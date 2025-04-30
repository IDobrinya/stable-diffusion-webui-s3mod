from dotenv import load_dotenv
import os

load_dotenv()

def get_env_var(key: str) -> str:
    value = os.getenv(key)
    return value
