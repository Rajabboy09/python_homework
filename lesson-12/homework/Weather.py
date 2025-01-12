import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('OPENWEATHER_API_KEY')
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

city_name = input("Enter the city name: ")

params = {
    'q': city_name,
    'appid': API_KEY,
    'units': 'metric' 
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    weather_data = response.json()

    print(f"Weather in {city_name.capitalize()}:")
    print(f"Temperature: {weather_data['main']['temp']}°C")
    print(f"Feels Like: {weather_data['main']['feels_like']}°C")
    print(f"Humidity: {weather_data['main']['humidity']}%")
    print(f"Pressure: {weather_data['main']['pressure']} hPa")
    print(f"Weather Description: {weather_data['weather'][0]['description'].capitalize()}")
    print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
else:
    print(f"Failed to fetch weather data for {city_name}. HTTP Status code: {response.status_code}")
