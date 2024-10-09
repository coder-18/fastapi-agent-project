import os
from dotenv import load_dotenv
from langchain.agents import Tool, initialize_agent
from langchain_openai import OpenAI
from app.tools import get_weather
from app.logger import logger

# Load environment variables from the .env file
load_dotenv()

# Function to load the OpenAI API key
def load_openai_api_key() -> str:
    """Loads the OpenAI API key from environment variables."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        logger.error("OpenAI API key is missing. Please set OPENAI_API_KEY in your .env file.")
        raise ValueError("OpenAI API key is missing. Please set OPENAI_API_KEY in your .env file.")
    logger.info("OpenAI API key loaded successfully.")
    return api_key

# Function to initialize the language model
def get_llm(openai_api_key: str) -> OpenAI:
    """
    Initializes and returns the OpenAI language model.

    Args:
        openai_api_key (str): The OpenAI API key for authentication.
    
    Returns:
        OpenAI: An initialized OpenAI LLM instance.
    """
    logger.info("Initializing OpenAI language model.")
    return OpenAI(openai_api_key=openai_api_key)

# Function to define the tools the agent can use
def get_tools() -> list:
    """
    Defines and returns the list of tools available for the agent.

    Returns:
        list: A list of Tool objects the agent can use.
    """
    logger.info("Initializing tools for the agent.")
    return [
        Tool(
            name="Weather Tool", 
            func=get_weather, 
            description="Get the weather for a given city."
        )
    ]

# Function to initialize and return the agent
def get_agent(verbose: bool = True) -> object:
    """
    Initializes and returns an agent with weather and crypto tools.

    Args:
        verbose (bool): If True, enables verbose mode for the agent. Defaults to True.

    Returns:
        object: The initialized agent.
    """
    # Load the OpenAI API key
    openai_api_key = load_openai_api_key()

    # Initialize the language model
    llm = get_llm(openai_api_key)

    # Define the tools the agent can use
    tools = get_tools()

    # Initialize and return the agent
    agent = initialize_agent(
        tools=tools, 
        llm=llm, 
        agent="zero-shot-react-description", 
        verbose=verbose
    )
    logger.info("Agent successfully initialized.")
    return agent

# Example usage
if __name__ == "__main__":
    try:
        agent = get_agent()
        # Now, you can use the agent to run queries like:
        result = agent.invoke("Get the weather for Paris.")
        print(result)
    except Exception as e:
        print(f"Error initializing the agent: {e}")
