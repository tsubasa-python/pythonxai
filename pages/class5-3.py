import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


messages = [{"role": "system", "content": "こんにちは。"}]

while True:
    user_input = input("くそみたいなお前:")
    if user_input.lower() in ["終わり"]:
        break

    messages.append({"role": "user", "content": user_input})

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
    )

    assistant_message = response.choices[0].message.content
    print(f"AI: {assistant_message}")
    messages.append({"role": "assistant", "content": assistant_message})
