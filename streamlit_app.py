from turtle import up
import streamlit as st
import asyncio
import os
import pandas as pd
from dotenv import load_dotenv
from models.model_client import get_model_client
from teams.document_intelligence import getDocumentIntelligenceTeam
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult

load_dotenv()

st.title("PPE Log Analysis")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

task = st.chat_input("Enter your task here...")

async def run_analyser_gpt(task: str, combined_task: str):
    try:
        gemini_model_client = get_model_client()
        team = getDocumentIntelligenceTeam(gemini_model_client)
        with st.chat_message("User", avatar="🧑‍💻"):
            st.markdown(task)
        async for message in team.run_stream(task=combined_task):
            if isinstance(message, TextMessage):
                if message.source.startswith('Data_Preparer_Agent'):
                    with st.chat_message('Data_Preparer_Agent', avatar="🛠️"):
                        st.markdown(message.content)
                elif message.source.startswith('Analyst_Agent'):
                    with st.chat_message('Analyst_Agent', avatar="🤖"):
                        st.markdown(message.content)
                elif message.source.startswith('Reporter_Agent'):
                    with st.chat_message('Reporter_Agent', avatar="📝"):
                        st.markdown(message.content)
            elif isinstance(message, TaskResult):
                #st.markdown(f'Stop Reason: {message.stop_reason}')
                st.markdown("Task Completed.")
        return None
    except Exception as e:
        st.error(f"Error: {e}")
        return e

if task:
    if uploaded_file is not None:
        if not os.path.exists("temp"):
            os.makedirs("temp", exist_ok=True)

        with open(os.path.join("temp", uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())

        try:
            file_data = pd.read_csv(os.path.join("temp", uploaded_file.name)).to_string(index=False)
        except Exception:
            file_data = "[Could not read file as CSV]"

        combined_task = f"{task}\n\nPPE Log Data:\n{file_data}"

        asyncio.run(run_analyser_gpt(task, combined_task))

    else:
        st.warning("Please upload a CSV log file.")
