from app.services import generate_response, generate_tokens

def test_generate_response_returns_echo():
    prompt = "Hello world"
    expected = "Echo: Hello world"
    assert generate_response(prompt) == expected

def test_generate_tokens_yields_expected_tokens():
    prompt = "Hello world"
    expected_tokens = ["Streaming ", "response ", "for: ", "Hello ", "world "]
    tokens = list(generate_tokens(prompt))
    assert tokens == expected_tokens
