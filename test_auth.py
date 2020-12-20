import time

from page_objects import AuthPage, MainPage


def test_auth_positive(browser):
    driver = browser
    default_alert_success_text = 'You are now logged in as First Last.'
    MainPage(driver).login_menu_click()
    AuthPage(driver).fill_login(email="test@test.com")
    AuthPage(driver).fill_password(passwd="12345")
    AuthPage(driver).login_btn_click()

    # сравниваем текст алерта с шаблоном
    alert_text = AuthPage(driver).get_alert_text()
    if default_alert_success_text in alert_text:
        assert True
    else:
        driver.save_screenshot("./screenshots/login_err.png")
        assert False