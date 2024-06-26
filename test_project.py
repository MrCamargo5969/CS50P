import pytest
import datetime
import sys
from project import user_exit, ai_response, user_speech, conversation_history

def test_user_exit(monkeypatch, capsys):
    monkeypatch.setattr(sys, 'exit', lambda: None)
    user_exit()
    captured = capsys.readouterr()
    assert "Exiting the chatbot. Goodbye!" in captured.out

def test_ai_response():
    conversation_history.clear()
    response = "Hello"
    ai_response(response)
    assert f'Bot: {response}' in conversation_history[-1]

def test_user_speech(monkeypatch):
    conversation_history.clear()
    monkeypatch.setattr('builtins.input', lambda _: 'test')
    assert user_speech() == 'test'
    assert 'User: test' in conversation_history[-1]