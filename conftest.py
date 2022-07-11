import logging
import pytest

from lib.weather_api import WeatherAPI

logging.basicConfig(level=logging.INFO)


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev",
                     help="environment to execute tests in ex: dev or qa - but qa is not implemented :)")

@pytest.fixture(autouse=True, scope='session')
def env(pytestconfig):
    """Initialize the Weather API for the test session with given environment"""
    return pytestconfig.getoption('env')

"""This function initializes Weather API Before Test starts"""
@pytest.fixture(autouse=True, scope='session', name='weather_api')
def initialize_white_hat_api(env):
        return WeatherAPI(env=env)