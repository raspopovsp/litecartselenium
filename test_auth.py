from page_objects import AuthPage, MainPage


def test_auth_positive(browser):
    MainPage(browser).login_menu_expand()
    AuthPage(browser).fill_login()
    AuthPage(browser).fill_password()
    AuthPage(browser).click_login()
