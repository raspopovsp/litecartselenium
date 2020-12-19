import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def browser(request):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    request.addfinalizer(driver.close)
    return driver
