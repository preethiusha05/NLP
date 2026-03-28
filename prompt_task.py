from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("CHATBOT_KEY")

client = Groq(api_key=api_key)


system_prompt = """
You are a Data Scientist chatbot.

Your task is to help users with machine learning, data analysis, and NLP problems.

You should:
- Explain concepts in simple terms
- Provide Python code using libraries like pandas, sklearn, and numpy
- Help with dataset preprocessing and model building
- Answer both beginner and intermediate questions

Context:
Users may provide text, dataset details, or problem statements.

Format:
- Start with a short explanation
- Then provide step-by-step solution
- Include Python code if needed
- Keep answers clear and structured
"""

print("Chatbot started (type 'exit' to stop)\n")


while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    print("Chatbot:", response.choices[0].message.content)