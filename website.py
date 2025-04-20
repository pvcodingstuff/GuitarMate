import os
import google.generativeai as genai
import gradio as gr
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Check if the API key is being loaded
api_key = os.getenv('GOOGLE_API_KEY')
print(f"API Key from environment: {api_key}")  

# Configure the Gemini API
genai.configure(api_key=api_key)

# Create the model
generation_config = {
    "temperature": 0.1,
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

def chatbot(user_input, chat_history=[]):
    formatted_history = []
    for turn in chat_history:
        formatted_history.append({"role": "user", "parts": [turn[0]]})
        formatted_history.append({"role": "model", "parts": [turn[1]]})

    chat_session = model.start_chat(history=formatted_history)
    response = chat_session.send_message(user_input)
    bot_response = response.text
    chat_history.append((user_input, bot_response))
    return bot_response, chat_history  # Return bot_response as the first value

# Create the Gradio interface
iface = gr.Interface(
    fn=chatbot,
    inputs=["text", gr.State([])],
    outputs=["text", "state"],
    title="MusicMate",
    description="Ask me anything about music theory or playing the guitar!",
    allow_flagging="never",
)

# Launch the Gradio interface
iface.launch(share=True)