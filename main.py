import os
import json

import streamlit as st
from groq import Groq


#streamlit page configuration
st.set_page_config(
    page_title="LLama 3.2 ChatBot",
    page_icon="🦙",
    layout="centered"
)

working_dir = os.path.dirname(os.path.abspath(__file__))
config_data = json.load(open(f"{working_dir}/config.json"))

GROQ_API_KEY = config_data["GROQ_API_KEY"]

#saving the api key in environment variable
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

client = Groq()

#initializing the chat history as streamlit session state of not present already
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


#streamlit page title
st.title="🦙LLAMA 3.1 ChatBot"

#display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


#input field for users message
user_prompt = st.chat_input("Ask LLAMA...")
if user_prompt:

    st.chat_message("user").markdown(user_prompt)

    st.session_state.chat_history.append({"role":"user","content":user_prompt})


    # send user message to llm and get a response
    messages = [
        {"role": "system", "content": "you are helpful assistant"},
        *st.session_state.chat_history
    ]

    response = client.chat.completions.create(

        model="llama-3.2-1b-preview",
        messages=messages
    )
    assistant_response=response.choices[0].message.content
    st.session_state.chat_history.append({"role":"assistant","content":assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)

    #to run
    #streamlit run / Users / salileshverma / Desktop / llama\ chatbot / src / main.py
    #http://192.168.137.27:8501/












