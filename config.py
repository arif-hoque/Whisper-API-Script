import os
from dotenv import load_dotenv

load_dotenv()

def get_config():
    return {
        "api_key": os.getenv("API_KEY"),
        "model": "whisper-1"  # Now part of config
    }