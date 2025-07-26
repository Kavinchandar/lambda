from fastapi import FastAPI, WebSocket
from fastapi.responses import JSONResponse
import asyncio

app = FastAPI()

# ---- REST Endpoint ----
@app.post("/chat")
async def chat(payload: dict):
    prompt = payload.get("prompt", "")
    response = generate_response(prompt)
    return JSONResponse({"response": response})

# ---- WebSocket Endpoint ----
@app.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            data = await websocket.receive_text()
            # Start streaming tokens
            for token in generate_tokens(data):
                await websocket.send_text(token)
                await asyncio.sleep(0.05)  # Simulate token streaming
        except Exception:
            break
    await websocket.close()

# ---- Dummy Response Generators ----
def generate_response(prompt: str):
    return f"Echo: {prompt}"

def generate_tokens(prompt: str):
    text = f"Streaming response for: {prompt}"
    for word in text.split():
        yield word + " "
