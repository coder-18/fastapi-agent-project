from fastapi import FastAPI, HTTPException
from app.agent import get_agent

app = FastAPI()

# Initialize the agent once
agent = get_agent()

@app.get("/")
def root():
    return {"message": "LangChain API is running!"}

@app.get("/ask")
def ask(query: str):
    """Endpoint to handle natural language queries."""
    try:
        result = agent.invoke(query)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Example usage: /ask?query=Get weather in London
    
    
