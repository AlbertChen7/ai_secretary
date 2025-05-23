
import google.generativeai as genai
from app.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def extract_intent_entities(message: str) -> tuple[str, list[str]]:
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"""
Given the following message: "{message}"

Extract:
- The user intent (e.g., 'request_routing', 'request_help', 'log_update', etc.)
- If specified, the team member name (Mike, Alice, etc)
- If specified, the nature of the role (plumber, electrician, construction, painter, etc). If no role was specified then denote it as 'unspecified'.

Format your response as:
Intent: <intent>
Name: <name>
Role: <role>

If unsure on any of these fields, fill field with "unknown".
"""

    response = model.generate_content(prompt)
    output = response.text

    try:
        lines = output.strip().splitlines()
        intent = lines[0].split(":")[1].strip()
        name = lines[1].split(":")[1].strip()
        role = lines[2].split(":")[1].strip()
    except Exception:
        intent, name, role = "unknown", "unknown", "unknown"

    return intent, name, role
