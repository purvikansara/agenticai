# app.py

import streamlit as st
from agent_builder import agent

st.title("🩺 Agentic AI Healthcare Assistant")
st.write("Ask me anything health-related, or request reminders and appointments!")

query = st.text_input("How can I help you today?")

if query:
    with st.spinner("Thinking..."):
        response = agent.run(query)
        st.success(response)

        # If response is a URL to image, display it
        if response.startswith("http") and response.endswith(".png"):
            st.image(response, caption="Generated Image")
