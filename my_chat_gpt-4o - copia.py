#!/usr/bin/env python
# coding: utf-8

# ### Preguntas y Respuestas con ChatGPT 4o

#!pip install openai
#!pip install streamlit
#!pip install streamlit openai
#!pip install python-dotenv

import openai
import streamlit as st
import os

from dotenv import load_dotenv

load_dotenv()

MyAPIKey = os.getenv('OPENAI_API_KEY')

openai.api_key = MyAPIKey

def is_goodbye(message):
    goodbye_keywords = ["adiós", "adios", "chao", "cerrar", "terminar", "bye"]
    return any(keyword in message.lower() for keyword in goodbye_keywords)

messages = []
def chat(user_input):
    messages = [
        {"role": "user", "content": user_input},
        {"role": "system", "content": ""}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=messages
    )

    return response.choices[0].message['content']

st.title("Chat con ChatGPT-4o")
response = openai.ChatCompletion.create(
  model="gpt-4o",
  messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "What can you do for me today?"},
  ]
)

bot_response = response.choices[0].message['content']
st.write(bot_response)

initial_message = st.text_input("Ingrese su pregunta:", key="initial_message")
messages = [{"role": "user", "content": initial_message}]

initial_message = st.text_input("Ingrese su pregunta:", key="initial_message")
messages = [{"role": "user", "content": initial_message}]

if st.button("Enviar"):
    user_input = initial_message

    response = chat(user_input)
    
    st.subheader("Respuesta:")
    st.write(response)

    if is_goodbye(user_input):
        st.info("Chat terminado.")
