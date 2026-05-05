
import streamlit as st
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

st.title("I am your AI Assistant")

openai_key = st.sidebar.text_input("Enter your OpenAI API key", type="password")

if not openai_key:
    st.info("Please enter your OpenAI API key to continue")
    st.stop()

# Optional: basic format check (Streamlit tutorial uses startswith validation)
if not openai_key.startswith("sk-"):
    st.warning("Please enter a valid OpenAI API key format (starts with sk-).")
    st.stop()

# Create once per session
if "llm" not in st.session_state:
    st.session_state.llm = ChatOpenAI(model="gpt-4o", api_key=openai_key)

question = st.text_input("Enter your question")

if question:
    try:
        response = st.session_state.llm.invoke([HumanMessage(content=question)])
        st.write(response.content)
    except Exception as e:
        st.error(f"Error: {e}")
