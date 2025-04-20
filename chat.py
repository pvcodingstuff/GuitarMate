import os
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key='AIzaSyBmBQRhQRTssd5Y9KxuS5aXS44G7ky6kAc')  # Directly pass your API key

# Create the model
generation_config = {
    "temperature": 0.8,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="You are an expert at teaching music theory and how to play guitar to people. Your task is to engage in conversations about guitar and music theory and answer questions. Explain music theory and guitar concepts/techniques so they are easily understandable. Ask questions so that you can better understand the user and improve the educational experience. Suggest way that these concepts can be related to the real world.",
)

history=[]

print("Bot: Hello, how can I help you?")

while True:

    user_input = input("You: ")

    chat_session = model.start_chat(
        history=history
    )

    response = chat_session.send_message(user_input)

    model_response = response.text

    print(f'Bot:{model_response}')
    print()

    history.append({"role" : "user", "parts": [user_input]})
    history.append({"role": "model", "parts": [model_response]})