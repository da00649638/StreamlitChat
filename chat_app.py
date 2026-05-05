import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

st.title("I am your AI Assistant")

openai_key = st.sidebar.text_input("Enter your OpenAI API key", type="password")

if not openai_key:
    st.info("Please enter your OpenAI API key to continue")
    st.stop()

if not openai_key.startswith("sk-"):
    st.warning("Please enter a valid OpenAI API key format (starts with sk-).")
    st.stop()

# Create once per session
if "llm" not in st.session_state:
    st.session_state.llm = ChatOpenAI(model="gpt-4o", api_key=openai_key)

# ✅ Initialize history once
if "messages" not in st.session_state:
    st.session_state.messages = [
        AIMessage(content="Hi! Ask me anything 🙂")
    ]

# ✅ Render chat history on every rerun
for msg in st.session_state.messages:
    role = "assistant" if isinstance(msg, AIMessage) else "user"
    with st.chat_message(role):
        st.markdown(msg.content)

# ✅ Chat input (better UX than st.text_input for chat)
prompt = st.chat_input("Enter your question")

if prompt:
    # Add user message to history + show it
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # ✅ Send entire conversation to model (history + new message)
        response = st.session_state.llm.invoke(st.session_state.messages)

        # Save assistant reply
        st.session_state.messages.append(AIMessage(content=response.content))

        with st.chat_message("assistant"):
            st.markdown(response.content)

    except Exception as e:
        st.error(f"Error: {e}")