
LOGS = []

def log_message(sender, body):
    LOGS.append({"from": sender, "message": body})
    print(f"Logged message: {body} from {sender}")
