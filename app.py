import os
from dotenv import load_dotenv
from groq import Groq

# Load env
load_dotenv()

# Create client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

print("Chatbot started (type 'exit' to stop)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chat ended.")
        break

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",   # fast & free model
            messages=[
                {"role": "user", "content": user_input}
            ]
        )

        print("Bot:", response.choices[0].message.content)

    except Exception as e:
        print("Error:", e)