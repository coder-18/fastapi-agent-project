import pytest
from unittest.mock import patch, MagicMock
from app.agent import load_openai_api_key, get_llm, get_agent


# Test for load_openai_api_key function
def test_load_openai_api_key_success(monkeypatch):
    """Test that the OpenAI API key is successfully loaded."""
    monkeypatch.setenv("OPENAI_API_KEY", "test_api_key")
    assert load_openai_api_key() == "test_api_key"


def test_load_openai_api_key_failure(monkeypatch):
    """Test that ValueError is raised when API key is missing."""
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    with pytest.raises(ValueError, match="OpenAI API key is missing"):
        load_openai_api_key()


# Test for get_llm function
def test_get_llm():
    """Test that the OpenAI LLM is initialized with the correct API key."""
    openai_api_key = "test_api_key"
    mock_llm = MagicMock()

    with patch(
        "app.agent.OpenAI", return_value=mock_llm
    ) as mock_openai_class:
        result = get_llm(openai_api_key)
        mock_openai_class.assert_called_once_with(
            openai_api_key=openai_api_key
        )
        assert result == mock_llm


# Test for get_agent function
@patch("app.agent.initialize_agent")
@patch("app.agent.get_llm")
@patch("app.agent.load_openai_api_key")
def test_get_agent(
    mock_load_openai_api_key, mock_get_llm, mock_initialize_agent
):
    """Test that the agent is successfully initialized."""
    mock_load_openai_api_key.return_value = "test_api_key"
    mock_llm_instance = MagicMock()
    mock_get_llm.return_value = mock_llm_instance
    mock_agent_instance = MagicMock()
    mock_initialize_agent.return_value = mock_agent_instance

    agent = get_agent(verbose=False)

    mock_load_openai_api_key.assert_called_once()
    mock_get_llm.assert_called_once_with("test_api_key")
    mock_initialize_agent.assert_called_once()
    assert agent == mock_agent_instance
