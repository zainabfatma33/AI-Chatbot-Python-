import json
import random
import re

# Load intents
with open('intents.json', 'r') as file:
    intents = json.load(file)

print("🤖 ChatPy: Hello! I'm your AI chatbot. Type 'quit' to exit.\n")

def get_response(user_input):
    user_input = user_input.lower()
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            # Simple matching
            if re.search(r'\b' + re.escape(pattern) + r'\b', user_input):
                return random.choice(intent['responses'])
    return "I'm not sure I understand. Can you say that differently?"

# Chat loop
while True:
    message = input("You: ")
    if message.lower() == "quit":
        print("🤖 ChatPy: Goodbye! Have a great day! 👋")
        break
    response = get_response(message)
    print("🤖 ChatPy:", response)
