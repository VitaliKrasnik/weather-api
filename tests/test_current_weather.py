
import pytest



class TestCurrentWeather():
    cities = [
        ("San Francisco"),
        ("Sacramento"),
        ("Winchester-On-The-Severn")
    ]

    @pytest.mark.smoke
    @pytest.mark.parametrize("city", cities)
    def test_current_weather(self, city, weather_api):
        """Make sure current weather endpoint returns correct response when correct parameters were specified"""
        response = weather_api.get_current_weather(city=city)
        response_body = response.json()

        assert response.status_code == 200, "Wrong response code"
        assert "location" in response_body, "There is no field 'location' in the response"
        assert "name" in response_body["location"], "There is no field 'name' in the response"
        assert "current" in response_body, "There is no field 'current' in the response"
        assert "temp_f" in response_body["current"], "There is no field 'temp_f' in the response"
        assert response_body["location"]["name"] == city, f"City name is not equal to {city}"


    def test_current_weather_empty_city_negative(self, weather_api):
        """Make sure current weather endpoint returns correct response code in response body when city parameter is empty"""
        city = ""
        response = weather_api.get_current_weather(city=city)
        response_body = response.json()

        assert response.status_code == 400, "Wrong response code"

        assert "error" in response_body, "There is no field 'error' in the response"
        assert "code" in response_body["error"], "There is no field 'code' in the response"
        assert "message" in response_body["error"], "There is no field 'message' in the response"

        expected_error_code = 1003
        assert response_body["error"]["code"] == expected_error_code, f"Error code is not equal to {expected_error_code}"
        expected_error_message = "Parameter q sholdn't be empy"
        assert response_body["error"]["message"] == expected_error_message, f"Error code is not equal to {expected_error_message}"

