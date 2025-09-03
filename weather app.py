import requests

API_KEY = "a25f949526804630aa6101540242101"
BASE_URL = "https://api.weatherapi.com/v1/current.json"


def get_weather(city):
    params = {
        "key": API_KEY, "q": city, "aqi": "no"}
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        weather_desc = data["current"]["condition"]["text"]
        temp_c = data["current"]["temp_c"]
        humidity = data["current"]["humidity"]
        wind_kph = data["current"]["wind_kph"]

        print(f"Weather in {city}: {weather_desc}")
        print(f"Temperature: {temp_c}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_kph} kph")
    else:
        print("Error fetching weather data:",
              response.status_code, response.text)


city_name = input("Enter city name: ")
get_weather(city_name)
