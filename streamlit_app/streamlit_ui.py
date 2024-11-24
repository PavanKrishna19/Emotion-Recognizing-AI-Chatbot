import sys
import os

# Add project root to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(project_root)

# Import the chatbot module
from app.chatbot import EmotionChatbot

import streamlit as st

# Load chatbot
chatbot = EmotionChatbot()

st.title("Emotion-Recognizing AI Chatbot")

user_input = st.text_area("Enter your message:")

if st.button("Predict Emotion"):
    if user_input.strip():
        emotion = chatbot.predict_emotion(user_input)
        st.write(f"Predicted Emotion: **{emotion}**")
    else:
        st.write("Please enter a valid message.")
