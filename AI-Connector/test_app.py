import io
import json
from contextlib import redirect_stdout
from app import main

def test_main_with_valid_chat_id():
    f = io.StringIO()
    
    with redirect_stdout(f):
        main(chat_id="test_chat_1", context_id="test_context_1")

    out = f.getvalue()
    result = json.loads(out)
    assert result["ok"] is True
    assert result["chat_id"] == "test_chat_1"
    assert "completion" in result

    print("test_main_with_valid_chat_id passed")


def test_main_with_missing_api_key(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    f = io.StringIO()

    with redirect_stdout(f):
        main(chat_id="some_chat")

    out = f.getvalue()
    result = json.loads(out)
    assert result["ok"] is False
    assert "API key missing" in result["error"]
    print("test_main_with_missing_api_key passed")


def test_main_with_missing_chat_id():
    f = io.StringIO()

    with redirect_stdout(f):
        main(chat_id=None)

    out = f.getvalue()
    result = json.loads(out)
    assert result["ok"] is False
    assert "chat_id is required" in result["error"]
    print("test_main_with_missing_chat_id passed")

if __name__ == "__main__":
    test_main_with_missing_api_key()
    test_main_with_missing_chat_id()
    test_main_with_valid_chat_id()
