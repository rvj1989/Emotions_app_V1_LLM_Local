import streamlit as st
from emotion_detector import detect_emotion
from prompt_builder import build_prompt
from llm_service import get_ai_reply
from db import add_log

st.set_page_config(page_title="Emotion_app_V1", page_icon="💬")
st.title("💬 Emotion_app_V1 - Chat with your AI buddy")

if "history" not in st.session_state:
    st.session_state["history"] = []  # list of (sender, message)

username = "User"  # for now, hard-coded; you can add login later

# Chat UI
for sender, message in st.session_state["history"]:
    if sender == username:
        st.chat_message("user").write(message)
    else:
        st.chat_message("assistant").write(message)

user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state["history"].append((username, user_input))
    emotion, all_scores = detect_emotion(user_input)
    prompt = build_prompt(user_input, emotion)
    ai_reply = get_ai_reply(prompt)

    # show AI reply
    st.session_state["history"].append(("AI", ai_reply))

    # log to DB
    add_log(username, user_input, emotion, prompt, ai_reply)

    st.rerun()  # refresh UI to show new messages
