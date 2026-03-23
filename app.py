from flask import Flask, render_template, request, jsonify
from huggingface_hub import InferenceClient
from duckduckgo_search import DDGS
import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

HF_TOKEN = os.getenv('HF_TOKEN')
if not HF_TOKEN:
    print("WARNING: HF_TOKEN not set. Create a .env file with your HuggingFace API key.")
    print("See .env.example for template.")
    
client = InferenceClient(api_key=HF_TOKEN)

def search_web(query):
    """Searches the live web for the latest info."""
    try:
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=4)
            return "\n".join([f"Source {i+1}: {r['body']}" for i, r in enumerate(results)])
    except Exception as e:
        print(f"Search Error: {e}")
        return "No recent internet data found."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({'reply': 'Error: No message provided'}), 400
        
        user_message = data.get('message', '').strip()
        if not user_message:
            return jsonify({'reply': 'Error: Empty message'}), 400

        web_context = search_web(user_message)
        today = datetime.datetime.now().strftime("%B %d, %Y")

        system_instruction = (
            f"You are the FinTrack AI Assistant. Today is {today}. "
            "Your goal is to provide SHORT, professional, and data-driven answers. "
            "1. Use bullet points for multiple facts. "
            "2. If a specific date is mentioned, focus ONLY on that. "
            "3. Do not give long introductions or apologies. "
            f"Use this live data to answer: \n{web_context}"
        )

        response = client.chat.completions.create(
            model="meta-llama/Llama-3.1-8B-Instruct",
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500
        )
        
        return jsonify({'reply': response.choices[0].message.content})
        
    except Exception as e:
        print(f"Error in /ask: {str(e)}")
        return jsonify({'reply': f"AI Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)