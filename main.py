# install: pip install ollama gradio

import gradio as gr
import ollama
import json
import re


MODEL_NAME = "llama3"  # change if needed


def extract_json(text):
    try:
        return json.loads(text)
    except:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group())
        return {"error": "Invalid JSON", "raw_output": text}


def analyze_review(review):

    prompt = f"""
You are a sentiment analysis engine.

Analyze the customer review and return ONLY valid JSON.

Tasks:
1. Determine sentiment: positive, negative, neutral, mixed
2. Extract exact positive phrases from review
3. Extract exact negative phrases from review
4. Generate one-line summary
5. Provide confidence score between 0.0 and 1.0
6. Recommendation: recommended | takeaway_only | dine_in | not_recommended

Review:
\"\"\"{review}\"\"\"

Return JSON in this format:

{{
  "sentiment": "mixed",
  "confidence": 0.88,
  "positive_phrases": [],
  "negative_phrases": [],
  "summary": "",
  "recommendation": ""
}}

IMPORTANT: Output ONLY JSON. No explanation.
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}]
    )

    raw_output = response["message"]["content"].strip()

    return extract_json(raw_output)


demo = gr.Interface(
    fn=analyze_review,
    inputs=gr.Textbox(label="Enter customer review"),
    outputs=gr.JSON(label="Sentiment Analysis Output"),
    title="Customer Review Sentiment Analyzer (Ollama)",
)

if __name__ == "__main__":
    demo.launch()