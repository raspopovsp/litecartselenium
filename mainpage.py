import time

from page_objects import MainPage


''' переход на страницу подменю Категорий '''
def test_goto_category(browser):
    driver = browser
    browser.get('http://localhost/index.php')
    MainPage(driver).accept_cookies()
    MainPage(driver).navigate_to(category='Rubber Ducks')
    assert 'rubber-ducks-c-1' in driver.current_url

