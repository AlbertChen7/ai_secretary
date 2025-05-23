
TEAM = [
    {"name": "Mike", "role": "plumber", "contact": "+15551234567"},
    {"name": "Alice", "role": "electrician", "contact": "+15559876543"},
]

def match_team_member(intent, name, role):
    for member in TEAM:
        if member["name"] == name:
            if role == "unspecified" or member["role"] == role:
                return member
        elif role == "unspecified" and member["role"] == role:
            return member
        elif member["role"] == role and name == "unknown":
            return member
    return None
