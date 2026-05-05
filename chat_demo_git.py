from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
import streamlit as st

st.title("I am your AI Assistant")

with st.sidebar:
    st.title("Provide your api key")
    OPENAI_API_KEY = st.text_input("Enter your OpenAI API key", type="password")
    llm = ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)


if not OPENAI_API_KEY:
    st.info("Please enter your OpenAI API key to continue")
    st.stop()

question = st.text_input("Enter your question")

if question:
    response = llm.invoke([
        HumanMessage(content=question)
    ])
    st.write(response.content)
