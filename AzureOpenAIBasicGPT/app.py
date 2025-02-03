import os
from dotenv import load_dotenv
from langchain_openai import AzureOpenAI
import streamlit as st

# Load environment variables
load_dotenv()

# Get Azure OpenAI configurations
azure_api_key = os.getenv("AZURE_OPENAI_API_KEY")
azure_endpoint = os.getenv("AZURE_OPENAI_API_BASE")  
azure_deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
azure_api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2023-03-15-preview")

# Check if all the necessary configurations are available
if not all([azure_api_key, azure_endpoint, azure_deployment_name]):
    st.error("Missing Azure OpenAI configuration. Please set AZURE_OPENAI_API_KEY, AZURE_OPENAI_API_BASE, and AZURE_OPENAI_DEPLOYMENT_NAME in your .env file.")
else:
    st.success("ChatGPT setup successful.. start using!!")

# Streamlit interface
st.title('Langchain Demo With Azure OpenAI API')

input_text = st.text_input("Search the topic you want")

# Initialize Azure OpenAI LLM
try:
    llm = AzureOpenAI(
        deployment_name=azure_deployment_name,   # Ensure no trailing slash
        api_key=azure_api_key,
        api_version=azure_api_version,
        azure_endpoint=azure_endpoint,           # Use azure_endpoint instead of base_url
        temperature=0.8
    )
except Exception as e:
    st.error(f"Failed to initialize Azure OpenAI: {e}")

if input_text:
    try:
        response = llm.invoke(input_text)
        st.write(response)
    except Exception as e:
        st.error(f"Error generating response: {e}")
