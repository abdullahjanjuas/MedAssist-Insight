# Configre Grok API Key
import os

def get_groq_api_key():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "GROQ_API_KEY not found. Set it as an environment variable."
        )
    return api_key
