import requests


class WeatherService:
    """API для работы с погодой и авто-настройкой под погоду"""
    def __init__(self):
        self.api_url = "http://api.weatherapi.com/v1/current.json"
        self.api_key = "17d15a49475b48aab79162932241706"
        self.geo_api_url = "http://ipinfo.io"

    def get_user_location(self):
        response = requests.get(self.geo_api_url)
        data = response.json()
        return data['city']  # выбираем конкретно ваш город

    def get_weather(self, city):
        params = {
            'key': self.api_key,
            'q': city,
        }
        response = requests.get(self.api_url, params=params)
        data = response.json()
        return {
            'temperature': data['current']['temp_c'],
            'condition': data['current']['condition']['text']
        }


weather_service = WeatherService()
city = weather_service.get_user_location()
print(f"Местность: {city}")
weather = weather_service.get_weather(city)
print(weather)
