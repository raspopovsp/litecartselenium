import pytest
from selenium import webdriver
from utilities import ReadConfig

base_url = ReadConfig.get_base_url()

def pytest_addoption(parser):
    parser.addoption("--url", action="store", default=base_url)
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture
def browser(request):
    browser_param = request.config.getoption("--browser")
    if browser_param == 'chrome':
        options = webdriver.ChromeOptions()
        # options.add_argument("user-data-dir=selenium")
        driver = webdriver.Chrome(options=options)
    elif browser_param == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception(f'{browser_param} is not supported')

    driver.implicitly_wait(5)
    request.addfinalizer(driver.close)
    driver.get(request.config.getoption("--url"))

    return driver
