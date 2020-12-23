from page_objects import AuthPage, MainPage
from utilities import ReadConfig

username = ReadConfig.get_username()
password = ReadConfig.get_password()

""" Позитивный тест авторизации """
def sleep_test_auth_positive(browser):
    driver = browser
    default_alert_success_text = 'You are now logged in as First Last.'
    MainPage(driver).login_menu_click()
    AuthPage(driver).fill_login(email=username)
    AuthPage(driver).fill_password(password=password)
    AuthPage(driver).login_btn_click()
    alert_text = AuthPage(driver).get_alert_text()
    if default_alert_success_text in alert_text:
        assert True
    else:
        driver.save_screenshot("./screenshots/login_err.png")
        assert False


"""" Тест авторизации существующего пользователя с запоминанием при последующим посещением """
def sleep_test_remember_me_checkbox(browser):
    driver = browser
    MainPage(driver).login_menu_click()
    AuthPage(driver).fill_login(email=username)
    AuthPage(driver).fill_password(password=password)
    AuthPage(driver).remember_me_check()
    AuthPage(driver).login_btn_click()
    # проверяем, что в кукис передался флаг remember
    cookies = driver.get_cookies()
    assert 'customer_remember_me' in cookies[0]['name']


""" Авторизации с незарегестрированным e-mail """
def test_unregistered_user_login(browser):
    driver = browser
    MainPage(driver).login_menu_click()
    AuthPage(driver).fill_login(email="blank@blank.com")
    AuthPage(driver).fill_password(password="______")
    AuthPage(driver).login_btn_click()
    if 'The email does not exist in our database' in AuthPage(driver).get_alert_text():
        assert True
    else:
        driver.save_screenshot("./screenshots/wrong_login_err.png")
        assert False, "Alert text error"

""" Авторизации с некорректным паролем """
def test_wrong_password(browser):
    driver = browser
    MainPage(driver).login_menu_click()
    AuthPage(driver).fill_login(email=username)
    AuthPage(driver).fill_password(password="______")
    AuthPage(driver).login_btn_click()
    if 'Wrong password or the account does not exist' in AuthPage(driver).get_alert_text():
        assert True
    else:
        driver.save_screenshot("./screenshots/wrong_password_err.png")
        assert False, "Alert text error"
