# agent_builder.py

import os
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from tools import set_reminder, book_appointment
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model_name="gpt-4", temperature=0)

tools = [
    Tool(
        name="Set Reminder",
        func=set_reminder,
        description="Use this to set a health-related reminder"
    ),
    Tool(
        name="Book Appointment",
        func=book_appointment,
        description="Use this to book an appointment"
    ),
    Tool(
        name="Health Info",
        func=lambda q: llm.predict(q),
        description="Use this to answer health-related questions"
    )
]

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
