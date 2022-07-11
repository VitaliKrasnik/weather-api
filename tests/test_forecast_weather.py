
import pytest



class TestCurrentWeather():
    forecast_test_data = [
        ("San Francisco", 2),
        ("Sacramento", 3),
        ("Winchester-On-The-Severn", 5)
    ]

    @pytest.mark.smoke
    @pytest.mark.parametrize("forecast_data", forecast_test_data)
    def test_forecast_weather(self, forecast_data, weather_api):
        expected_forecast_city = forecast_data[0]
        expected_forecast_num_of_days = forecast_data[1]
        response = weather_api.get_weather_forecast(city=expected_forecast_city, days=expected_forecast_num_of_days)
        response_body = response.json()

        assert response.status_code == 200, "Wrong response code"
        assert "location" in response_body, "There is no field 'location' in the response"
        assert "name" in response_body["location"], "There is no field 'name' in the response"
        assert "forecast" in response_body, "There is no field 'current' in the response"
        assert "forecastday" in response_body["forecast"], "There is no field 'name' in the response"


        assert response_body["location"]["name"] == expected_forecast_city, f"City name is not equal to {expected_forecast_city}"
        actual_forecast_num_of_days = len(response_body["forecast"]["forecastday"])
        assert actual_forecast_num_of_days  == expected_forecast_num_of_days, f"Number of forecasts doesn't match to expected number {expected_forecast_num_of_days}"



