import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--url", "-U", action="store", default="http://localhost", help="url basic")


@pytest.fixture
def browser(request):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    request.addfinalizer(driver.close)
    driver.get(request.config.getoption("--url"))
    return driver
