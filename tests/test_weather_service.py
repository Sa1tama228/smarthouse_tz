from weather_service import WeatherService

def test_get_weather(monkeypatch):
    weather_service = WeatherService()

    def mock_get(*args, **kwargs):
        class MockResponse:
            def json(self):
                return {
                    'current': {
                        'temp_c': 20.0,
                        'condition': {
                            'text': 'Sunny'
                        }
                    }
                }
        return MockResponse()

    monkeypatch.setattr('requests.get', mock_get)
    weather = weather_service.get_weather('Test City')
    assert weather['temperature'] == 20.0
    assert weather['condition'] == 'Sunny'
