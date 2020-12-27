import time

from selenium.webdriver.common.by import By

from page_objects import UserRegistration, MainPage

alert_success = 'Your customer account has been created.'
alert_error = 'The email address already exists in our customer database.'

customer_data = {
    'company': 'new company',
    'tax_id': 'new tax id',
    'first_name': 'first name',
    'last_name': 'last name',
    'address_1': 'street',
    'address_2': 'building',
    'postal_code': '1234',
    'city': 'of midnight',
    'country': 'AU',
    'state': 'VIC',
    'email': 'new@mail.com',
    'phone': '1234567890',
    'password': '12345',
    'password_confirmation': '12345',
}


""" Регистрация нового покупателя """
def sleep_test_create_customer(browser):
    driver = browser
    MainPage(driver).accept_cookies()
    MainPage(driver).login_menu_click()
    MainPage(driver).goto_create_customer()
    UserRegistration(driver).customer_data(customer_data)
    UserRegistration(driver).privacy_checkbox_click()
    UserRegistration(driver).create()
    alert = UserRegistration(driver).get_alert_text()
    if alert_success in alert:
        if 'create_account' not in driver.current_url:
            assert True
        else:
            assert False
    else:
        assert False

""" Попытка регистрации, уже зарегестрированного покупателя """
def test_create_customer_with_duplicated_email(browser):
    driver = browser
    MainPage(driver).accept_cookies()
    MainPage(driver).login_menu_click()
    MainPage(driver).goto_create_customer()
    UserRegistration(driver).customer_data(customer_data)
    UserRegistration(driver).privacy_checkbox_click()
    UserRegistration(driver).create()
    time.sleep(3)
    alert = UserRegistration(driver).get_alert_text()
    if alert_error in alert:
        if 'create_account' in driver.current_url:
            assert True
        else:
            assert False
    else:
        assert False

# def test_inputs(browser):
#     driver = browser
#     MainPage(driver).accept_cookies()
#     MainPage(driver).login_menu_click()
#     MainPage(driver).goto_create_customer()
#     controls = driver.find_elements(By.CLASS_NAME, 'form-control')
#     for control in controls:
#         print(control.get_attribute('type'))
#     time.sleep(3)