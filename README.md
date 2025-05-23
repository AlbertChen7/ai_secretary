# AI Secretary with Vonage and Gemini

This project sets up a FastAPI backend for routing construction site messages using Vonage for SMS and Gemini 1.5 Flash for NLP.

Start api with:
uvicorn app.main:app --reload
Expose api to internet with:
ngrok http http://127.0.0.1:8000                                 