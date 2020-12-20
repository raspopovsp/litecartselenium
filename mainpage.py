import time

from page_objects import MainPage

''' переход на страницу подменю Категорий '''


def test_goto_category(browser):
    driver = browser
    # MainPage(driver).accept_cookies()
    MainPage(driver).navigate_to(category='Rubber Ducks')
    assert 'rubber-ducks-c-1' in driver.current_url


''' Меню авторизации закрыто по умолчанию '''
def test_account_menu_closed_by_default(browser):
    driver = browser
    if MainPage(driver).is_expanded():
        assert False
    else:
        assert True


''' Меню авторизации открывается при клике '''
def test_account_menu_expand(browser):
    driver = browser
    if not MainPage(driver).is_expanded():
        MainPage(driver).login_menu_click()
        if MainPage(driver).is_expanded():
            assert True
        else:
            assert False
    else:
        raise Exception("Menu expanded")
