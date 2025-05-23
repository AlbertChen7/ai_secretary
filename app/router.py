
from app.nlp import extract_intent_entities
from app.team_directory import match_team_member
from app.storage import log_message

async def handle_message(body: str, sender: str) -> str:
    intent, name, role = extract_intent_entities(body)
    member = match_team_member(intent, name, role)

    if member:
        return [f"You will be connected with {member['name']} at {member['contact']}.", intent, name, role]
    else:
        log_message(sender, body)
        return ["Thanks! Your message has been logged for the team to review.", intent, name, role]
