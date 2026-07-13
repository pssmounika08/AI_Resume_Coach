import os
from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()


def get_gemini_model():
    api_key = None

    try:
        if hasattr(st, "secrets") and "OPENROUTER_API_KEY" in st.secrets:
            api_key = st.secrets["OPENROUTER_API_KEY"]
    except Exception:
        api_key = None

    if not api_key:
        api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENROUTER_API_KEY not found. Set it in Streamlit secrets or your local .env file."
        )

    client = OpenAI(
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1"
    )

    return client