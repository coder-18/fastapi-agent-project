import requests
from dotenv import load_dotenv
from app.utils import load_config
import os

# Load environment variables from the .env file
load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# Load the configuration from config.yaml
config = load_config("config.yaml")


# Tool 1: OpenWeather API
def get_weather(city: str) -> str:
    """Fetches current weather for a given city using the OpenWeather API."""
    api_key = WEATHER_API_KEY
    base_url = config["weatherapi"]["base_url"]
    units = config["weatherapi"]["units"]

    url = f"{base_url}?q={city}&appid={api_key}&units={units}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return f"""The weather in {city} is {data['weather'][0]['description']}
          with a temperature of {data['main']['temp']}°C."""
    else:
        return (
            f"Could not retrieve weather data for {city}. Please try again."
        )
