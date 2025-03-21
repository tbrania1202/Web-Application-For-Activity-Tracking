import json

MESSAGES_FILE = "app/messages.json"

def load_messages():
    try:
        with open(MESSAGES_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def save_messages(messages):
    with open(MESSAGES_FILE, "w", encoding="utf-8") as file:
        json.dump(messages, file, indent=4)

def add_message(new_message):
    if new_message:
        messages = load_messages()
        messages.append(new_message)

        messages = messages[-5:]
        save_messages(messages)