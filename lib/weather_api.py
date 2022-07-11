import json
import logging
import requests
from requests import Response

from data.env_data import env_data
logging.basicConfig(level=logging.INFO)

class WeatherAPI:

    def __init__(self, env='dev'):
        try:
            self.base_url = env_data[env]["base_url"]
            self.api_key = env_data[env]["api_key"]
            logging.info('Initialized Weather API for ENV: %s', env)
        except KeyError:
            raise KeyError('Unsupported Environment')

    def get_current_weather(self, city="San Francisco", aqi="no"):
        logging.info(f"Getting information Current weather in {city}")
        params = {"key": self.api_key, "q": city, "aqi": "no"}
        response = requests.get(f"{self.base_url}/current.json", params=params)
        self.assert_response_json(response)
        return response

    def get_weather_forecast(self, city="San Francisco", days=1, aqi="no", alerts="no"):
        logging.info(f"Getting information of weather forecast in {city} for {days} day(s)")
        params = {"key": self.api_key, "q": city, "aqi": aqi, "days": days, "alerts": alerts}

        response = requests.get(f"{self.base_url}/forecast.json", params=params)
        self.assert_response_json(response)
        return response

    """Make sure the response was returned in JSON format"""
    @staticmethod
    def assert_response_json(response: Response):
        try:
             response.json()
        except json.JSONDecodeError:
            assert False, f" Response is not in JSON format.\n Response text is '{response.text}' for Request: \n {response.history[0]} "
