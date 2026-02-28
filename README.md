📊 Customer Review Sentiment Analyzer (Ollama + Gradio)
Overview

This project analyzes customer reviews using a local LLM (LLaMA3 via Ollama).
It extracts structured insights including:

Sentiment (positive / negative / neutral / mixed)

Confidence score

Positive phrases

Negative phrases

One-line summary

Recommendation

The app runs locally using Gradio for UI and Ollama for model inference.

🛠 Tech Stack

Python

Ollama (LLaMA3)

Gradio

JSON Parsing

📁 Project Structure
sentimentAnalysis/
│
├── app.py
├── requirements.txt
└── README.md
⚙️ Setup Instructions
1. Install Ollama

Download and install from:
https://ollama.com

2. Pull LLaMA3 Model
ollama pull llama3
3. Create Virtual Environment (optional)
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
4. Install Dependencies
pip install gradio ollama
▶️ Run the Application
python app.py

The app will open at:

http://127.0.0.1:7860
🧠 How It Works

User enters a review.

Prompt is sent to LLaMA3 via Ollama.

Model returns structured JSON.

JSON is validated and displayed in UI.

📌 Example Output
{
  "sentiment": "mixed",
  "confidence": 0.87,
  "positive_phrases": ["delicious food"],
  "negative_phrases": ["slow service"],
  "summary": "Great food but service needs improvement.",
  "recommendation": "takeaway_only"
}
