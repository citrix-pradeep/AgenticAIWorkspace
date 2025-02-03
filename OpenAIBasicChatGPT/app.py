import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
import streamlit as st

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API key from environment
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    st.error("Missing OpenAI API key. Please set it in a .env file.")

# Streamlit interface
st.title('Langchain Demo With OPENAI API')

input_text = st.text_input("Search the topic you want")

# Initialize OpenAI LLM
try:
    llm = OpenAI(temperature=0.8, openai_api_key=openai_api_key)
except Exception as e:
    st.error("Failed to initialize OpenAI. Please check your API key.")

if input_text:
    try:
        response = llm.invoke(input_text)
        st.write(response)
    except Exception as e:
        st.error(f"Error generating response: {e}")
