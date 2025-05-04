# weather_service.py: OpenWeatherMap API integration for daily weather
import httpx
from app.config import settings
from datetime import date

async def get_weather_data(location: dict, date: date) -> dict:
    """Fetch weather data for a specific location and date"""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={
                "lat": location["latitude"],
                "lon": location["longitude"],
                "appid": settings.OPENWEATHER_API_KEY,
                "units": "metric"
            }
        )
        response.raise_for_status()
        data = response.json()

    return {
        "temperature": data["main"]["temp"],
        "precipitation": data.get("rain", {}).get("1h", 0),
        "humidity": data["main"]["humidity"]
    }