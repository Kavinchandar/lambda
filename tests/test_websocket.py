import pytest
import asyncio
import websockets

@pytest.mark.asyncio
async def test_websocket_chat():
    uri = "ws://localhost:8000/ws/chat"
    test_message = "Hello, this is a test message."
    expected_start = "Streaming response for: "

    async with websockets.connect(uri) as websocket:
        await websocket.send(test_message)

        full_response = ""
        try:
            while True:
                response = await asyncio.wait_for(websocket.recv(), timeout=2)
                full_response += response
        except asyncio.TimeoutError:
            pass  # Streaming likely complete

        expected_response = expected_start + test_message

        # Strict equality check
        assert full_response.strip() == expected_response.strip()
