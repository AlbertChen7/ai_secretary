
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
VONAGE_API_KEY = os.getenv("VONAGE_API_KEY")
VONAGE_API_SECRET = os.getenv("VONAGE_API_SECRET")
