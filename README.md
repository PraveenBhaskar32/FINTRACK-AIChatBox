# 📈 FinTrack AI | Agentic Financial Advisor

FinTrack AI is a modern financial dashboard that combines a sleek UI with a high-performance **AI-Powered Chatbox**. Instead of relying on static data, this platform uses an agentic workflow to research the live web, providing users with real-time financial insights and market analysis.

---

## 🤖 The AI Chatbox: Retrieval-Augmented Generation (RAG)

The heart of this project is the **Agentic Chat Assistant**. Unlike standard chatbots, this assistant doesn't just "chat"—it researches. It is powered by a custom **RAG (Retrieval-Augmented Generation)** pipeline.

### 🧠 How the AI Brain Works
When you ask a question like *"What is the current trend for Nvidia stock?"* or *"Should I invest in Gold today?"*, the AI follows a 3-step process:

1.  **Web Retrieval:** The system identifies the need for real-time data and triggers the **DuckDuckGo Search API** to scan the latest financial news and market reports.
2.  **Context Augmentation:** The top search results are parsed and injected into the AI's "short-term memory" as factual context.
3.  **Llama 3.1 Reasoning:** Using the **Meta Llama-3.1-8B-Instruct** model (via Hugging Face), the agent synthesizes the live data and the user query to provide a professional, data-backed response.



### ⚡ Key AI Features
* **Zero Knowledge Cutoff:** By using live web search, the AI is always aware of market moves that happened minutes ago.
* **Hallucination-Free:** Every financial insight is grounded in real-time search results, drastically reducing the "guessing" common in standard AI.
* **Agentic Decision Making:** The system intelligently decides *when* to search the web and *when* to use its internal reasoning.

---

## 🛠️ Tech Stack

* **Backend:** Python & Flask
* **LLM:** Llama 3.1 (8B Instruct) 
* **Inference:** Hugging Face API
* **Search Engine:** DuckDuckGo Search API
* **Frontend:** Custom CSS/JS Fintech Dashboard
* **Deployment:** Render Cloud

---

## 📂 Folder Structure

```text
├── app.py              # Main Flask server & AI/RAG logic
├── requirements.txt    # Production-ready dependencies
├── static/             # CSS and JavaScript assets
├── templates/          # HTML Structure (Dashboard & Chat Widget)
└── .gitignore          # Security shield for private tokens
