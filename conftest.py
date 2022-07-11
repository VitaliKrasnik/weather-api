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

@pytest.fixture(autouse=True, scope='session', name='weather_api')
def initialize_white_hat_api(env):
    """Initializes Weather API Before Test starts"""
    return WeatherAPI(env=env)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    test_fn = item.obj
    docstring = getattr(test_fn, '__doc__')
    if docstring:
        report.nodeid = docstring