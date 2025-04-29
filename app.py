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
