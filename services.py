from app.models import Item
from fastapi import HTTPException

# ---- Dummy Response Generators ----
def generate_response(prompt: str):
    return f"Echo: {prompt}"

def generate_tokens(prompt: str):
    text = f"Streaming response for: {prompt}"
    for word in text.split():
        yield word + " "