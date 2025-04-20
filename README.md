# GuitarMate
Your new companion to teach you guitar and music theory!

Learning music theory and guitar can be challenging and often feels isolating. We wanted to create an accessible and engaging way for aspiring musicians to learn at their own pace, with personalized guidance from an AI.

## What it does

GuitarMate is an AI-powered chatbot designed to:

1. Teach Music Theory: Explain concepts like scales, chords, rhythm, and harmony in an easy-to-understand way.
2. Guide Guitar Learning: Provide information on basic chords, strumming patterns, fingerpicking techniques, and even suggest songs to learn.
3. Offer Personalized Feedback: Respond to specific questions and provide tailored explanations based on the user's level and inquiries.

## How we built it

For the chatbot we leveraged the power of the Gemini-1.5-Flash model to create an intelligent and conversational tutor capable of understanding and responding to music-related questions.
We also built a user-friendly web interface using Gradio to host the chatbot, making it easily accessible through a web browser.

## Challenges we ran into

We put our API key into a .env file but the library wasn't taking it. To troubleshoot this we used the print function to print our API key and it said none meaning that something was wrong in our code. We eventually realised we forgot to configure the gemini API so our key wasn't being authenticated. We also had lots of trouble implementing history.

## Accomplishments that we're proud of

* Successfully creating a functional AI chatbot capable of engaging in meaningful conversations about music theory and guitar.
* Developing a web interface that makes the chatbot accessible and easy to use.


## Team

* Pradyun Vemula - Built the chatbot
* Ruthvik Komal Polukonda - Implemented chatbot into gradio website

## Acknowledgements

* We would like to thank the organizers of FH7 for providing this opportunity.
* Special thanks to the developers of the Gemini model and Gradio for their powerful tools.
