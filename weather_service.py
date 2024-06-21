import requests


class WeatherService:
    """API для работы с погодой и авто-настройкой под погоду"""
    def __init__(self):
        self.api_url = "http://api.weatherapi.com/v1/current.json"
        self.api_key = "17d15a49475b48aab79162932241706"
        self.geo_api_url = "http://ipinfo.io"

    def get_user_location(self):
        try:
            response = requests.get(self.geo_api_url)
            response.raise_for_status()
            data = response.json()
            return data['city']  # выбираем конкретно ваш город
        except requests.RequestException as e:
            print(f"Ошибка получения геолокации: {e}")
            return None

    def get_weather(self, city):
        try:
            params = {
                'key': self.api_key,
                'q': city,
            }
            response = requests.get(self.api_url, params=params)
            response.raise_for_status()
            data = response.json()
            return {
                'temperature': data['current']['temp_c'],
                'condition': data['current']['condition']['text']
            }
        except requests.RequestException as e:
            print(f"Ошибка получения погоды: {e}")
            return None


weather_service = WeatherService()
city = weather_service.get_user_location()
if city:
    print(f"Местность: {city}")
    weather = weather_service.get_weather(city)
    if weather:
        print(weather)
else:
    print("Не удалось определить местоположение")
