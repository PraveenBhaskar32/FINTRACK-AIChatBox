# FinTrack AI Chatbox Web

A Flask-based AI chatbot with web interface that uses HuggingFace's Llama LLM and live web search capabilities.

## Features
- Real-time web search integration (DuckDuckGo)
- AI-powered responses using HuggingFace Inference API
- Beautiful chat UI with responsive design
- Live market data display

## Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Up Environment Variables
```bash
cp .env.example .env
# Edit .env and add your HuggingFace API key
```

Get your API key from: https://huggingface.co/settings/tokens

### 3. Run the Application
```bash
python app.py
```

The app will start at `http://localhost:5000`

## Files Overview
- **app.py** - Main Flask application with API routes
- **train.py** - Naive Bayes model training (optional, not used in current version)
- **intents.json** - Sample intents data
- **templates/index.html** - Web UI
- **static/style.css** - Styling

## Usage
1. Open http://localhost:5000 in your browser
2. Click the robot icon in the bottom right
3. Type your question and send
4. The AI will search the web and provide an answer

## Fixed Issues
✓ Exposed API key moved to environment variables
✓ XSS vulnerability fixed with proper HTML escaping
✓ Better error handling and validation
✓ Improved async error catching in frontend
