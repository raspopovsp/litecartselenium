from page_objects import AuthPage, MainPage, BasePage
from utilities import ReadConfig

username = ReadConfig.get_username()
password = ReadConfig.get_password()


""" Позитивный тест авторизации """
def sleep_test_auth_positive(browser):
    BasePage.logger.info('========== test auth positive start =========')
    driver = browser
    default_alert_success_text = 'You are now logged in as First Last.'
    MainPage(driver).login_menu_click()
    AuthPage(driver).fill_login(email=username)
    AuthPage(driver).fill_password(password=password)
    AuthPage(driver).login_btn_click()
    alert_text = AuthPage(driver).get_alert_text()
    if default_alert_success_text in alert_text:
        BasePage.logger.info('========== TEST PASSED =========')
        assert True
    else:
        driver.save_screenshot("./screenshots/login_err.png")
        assert False, BasePage.logger.info('========== TEST FAILED =========')


"""" Тест авторизации существующего пользователя с запоминанием при последующим посещением """
def sleep_test_remember_me_checkbox(browser):
    driver = browser
    BasePage.logger.info('========== login with remember me start =========')
    MainPage(driver).login_menu_click()
    AuthPage(driver).fill_login(email=username)
    AuthPage(driver).fill_password(password=password)
    AuthPage(driver).remember_me_check()
    AuthPage(driver).login_btn_click()
    # проверяем, что в кукис передался флаг remember
    cookies = driver.get_cookies()
    if 'customer_remember_me' in cookies[0]['name']:
        BasePage.logger.info('========== TEST PASSED =========')
        assert True
    else:
        assert False, BasePage.logger.info('========== TEST FAILED =========')


""" Авторизации с незарегестрированным e-mail """
def sleep_test_unregistered_email_login(browser):
    driver = browser
    BasePage.logger.info('========== unregistered email test start =========')
    MainPage(driver).login_menu_click()
    AuthPage(driver).fill_login(email="blank@blank.com")
    AuthPage(driver).fill_password(password="______")
    AuthPage(driver).login_btn_click()
    if 'The email does not exist in our database' in AuthPage(driver).get_alert_text():
        BasePage.logger.info('========== TEST PASSED =========')
        assert True
    else:
        driver.save_screenshot("./screenshots/wrong_login_err.png")
        assert False, BasePage.logger.info('========== TEST FAILED =========')


""" Авторизации с некорректным паролем """
def sleep_test_wrong_password(browser):
    driver = browser
    BasePage.logger.info('========== wrong password test start =========')
    MainPage(driver).login_menu_click()
    AuthPage(driver).fill_login(email=username)
    AuthPage(driver).fill_password(password="______")
    AuthPage(driver).login_btn_click()
    if 'Wrong password or the account does not exist' in AuthPage(driver).get_alert_text():
        BasePage.logger.info('========== TEST PASSED =========')
        assert True
    else:
        driver.save_screenshot("./screenshots/wrong_password_err.png")
        assert False, BasePage.logger.info('========== TEST FAILED =========')