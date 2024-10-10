# LangChain Agent for Public APIs

This project demonstrates a LangChain agent deployed using **FastAPI**, which can query public APIs such as **OpenWeather API** to fetch real-time weather data.

## Features:
- Query the **OpenWeather API** to fetch current weather data for any city.
- Easily extensible to work with other public APIs.
- Deployed using **FastAPI** for handling HTTP requests.
- Uses **LangChain** to facilitate the interaction with APIs.
- Ready for Docker deployment.

---

## Prerequisites

Before running this project, ensure you have the following installed:

- **Python 3.8+**
- **Git** (for version control)
- **OpenWeather API Key** (You can obtain this from [OpenWeather API](https://openweathermap.org/api))
- **FastAPI** and other dependencies (specified in `requirements.txt`)

### OpenWeather API Key Setup
Create a `.env` file in the root directory and add your OpenWeather API key:

## Install Dependencies
   ```bash
   pip install -r requirements.txt
   ```
# Usage
## Running server:
Inside the LANGCHAIN_AGENT_DEMO directory, start the API using the below command. Make sure you have added the OPENAI_API_KEY and WEATHER_API_KEY to you environment variables
```
uvicorn app.app:app --reload
```
The FastAPI server will be available at http://127.0.0.1:8000.

## Query the API: 
You can access the FastAPI documentation and test the endpoints using the automatically generated Swagger UI at
```
http://127.0.0.1:8000/docs
```
Example endpoint to get weather for a city:
```
GET /weather/{city}
```
## Example curl request:
```
curl -X 'GET' \
'http://127.0.0.1:8000/weather/London' \
-H 'accept: application/json'
```

# Testing
## Running Unit Tests
Unit tests are included to ensure the functionality of the agent. You can run tests using pytest:

Run tests locally:
```
pytest
```

# Docker Setup
You can containerize the application and run it using Docker for easy deployment.

1. Build Docker Image
```
sudo docker build -t fastapi-agent-app .
```
2. Run the Docker Container
```
sudo docker run -d --name fastapi-agent-container -p 8000:8000 fastapi-agent-app
```

```
fastapi-agent-project/
├── app/
│   ├── __init__.py
│   ├── app.py            # FastAPI main app
│   ├── agent.py          # LangChain agent to get weather info
│   ├── logger.py         # Logger setup
│   ├── tools.py          # Helper functions like `get_weather`
│   ├── utils.py          # Utility functions
├── tests/
│   ├── test_agent.py      # Unit tests for agent
├── .env                   # Environment variables (API keys, etc.)
├── logging_config.yaml     # Logging configuration
├── requirements.txt        # Python dependencies
├── Dockerfile              # Dockerfile for containerization
├── .dockerignore           # Ignore unnecessary files in Docker builds
├── pytest.ini              # pytest configuration
└── README.md               # Project documentation

```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
If you have any questions or issues, feel free to contact me:

GitHub: @coder-18 \
Email: sendittomohnish@gmail.com