from jsonpickle import json

from page_objects import UserRegistration, MainPage
from utilities import StringGenerator, db_connector
from utilities import LogGenerator

logger = LogGenerator.loggen()

alert_success = 'Your customer account has been created.'
alert_error = 'The email address already exists in our customer database.'
pass_confirmation_alert = 'The passwords did not match'

customer_data_const = {
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

customer_data_generated = {
    'company': StringGenerator.random_string(letters=True, digits=True, punctuation=True, whitespaces=10, size=10),
    'tax_id': StringGenerator.random_string(letters=False, digits=True, punctuation=False, whitespaces=0, size=10),
    'first_name': StringGenerator.random_string(letters=True, digits=True, punctuation=True, whitespaces=10, size=10),
    'last_name': StringGenerator.random_string(letters=True, digits=True, punctuation=True, whitespaces=10, size=10),
    'address_1': StringGenerator.random_string(letters=True, digits=True, punctuation=True, whitespaces=10, size=16),
    'address_2': StringGenerator.random_string(letters=True, digits=True, punctuation=True, whitespaces=10, size=16),
    #  POSTAL_CODE для Австралии 4 цифры. Для случайного выбор стран выключить.
    #  TODO: Написать рандомайзер для индекса на основнии регэкспа
    'postal_code': StringGenerator.random_string(letters=False, digits=True, punctuation=False, size=4, whitespaces=0),
    'city': StringGenerator.random_string(letters=True, digits=True, punctuation=True, whitespaces=10, size=10),
    'country': 'AU',
    'state': 'VIC',
    'email': StringGenerator.random_string(letters=True, digits=True, punctuation=False, whitespaces=0,
                                           size=10) + '@mail.com',
    'phone': StringGenerator.random_string(letters=False, digits=True, punctuation=False, whitespaces=0, size=10),
    'password': StringGenerator.random_string(letters=True, digits=True, punctuation=True, whitespaces=0, size=10),
    'password_confirmation': None  # Заполняется отдельно
}
customer_data_generated['password_confirmation'] = customer_data_generated['password']


""" Регистрация нового покупателя """
def sleep_test_create_customer(browser):
    driver = browser
    logger.info('TEST CREATE USER START')
    MainPage(driver).accept_cookies()
    MainPage(driver).login_menu_click()
    MainPage(driver).goto_create_customer()
    UserRegistration(driver).customer_data(customer_data_generated)
    UserRegistration(driver).privacy_checkbox_click()
    UserRegistration(driver).create()
    alert = UserRegistration(driver).get_alert_text()
    if alert_success in alert:
        if 'create_account' not in driver.current_url:
            logger.info(f'new customer with {customer_data_generated["email"]} created')
            assert True
        else:
            logger.error('Not relocated to index page')
            driver.save_screenshot('screenshots/register_fail.png')
            assert False, 'wrong URL (expect: index page)'
    else:
        logger.error('customer not created')
        assert False, 'alert success not detected'


""" Тест регистрации с уже существующим в системе e-mail """
def sleep_test_create_customer_with_duplicated_email(browser):
    driver = browser
    MainPage(driver).accept_cookies()
    MainPage(driver).login_menu_click()
    MainPage(driver).goto_create_customer()
    UserRegistration(driver).customer_data(customer_data_generated)
    UserRegistration(driver).privacy_checkbox_click()
    UserRegistration(driver).create()
    alert = UserRegistration(driver).get_alert_text()
    if alert_error in alert:
        logger.info(f'Alert danger: {alert[:1]} appearance')
        if 'create_account' in driver.current_url:
            logger.info(f'new customer with {customer_data_generated["email"]} already registered')
            assert True
        else:
            logger.error(f'Customer with duplicated email {customer_data_generated["email"]}\
                                  registered and user redirected to {driver.current_url}')
            assert False, 'user registered and relocated to index'
    else:
        logger.error(f'Alert danger: {alert[1:]} not appears')
        assert False, 'Alert danger not appears'


''' Тестирование регистрации с ошибкой при подтверждении пароля '''
def sleep_test_user_registration_with_wrong_confirmation_pass(browser):
    driver = browser
    MainPage(driver).accept_cookies()
    MainPage(driver).login_menu_click()
    MainPage(driver).goto_create_customer()
    customer_data_generated['password_confirmation'] = ""
    UserRegistration(driver).customer_data(customer_data_generated)
    UserRegistration(driver).privacy_checkbox_click()
    UserRegistration(driver).create()
    alert = UserRegistration(driver).get_alert_text()
    if pass_confirmation_alert in alert:
        logger.info(f'Password confirmation alert: {alert[1:]} appearance')
        if 'create_account' in driver.current_url:
            logger.info(f'Password confirmation exception')
            assert True
        else:
            logger.error(f'Customer with unconfirmed password registered')
            assert False, 'user registered and relocated to index'
    else:
        logger.error(f'Password confirmation alert: {alert[1:]} not appears')
        assert False, 'Password confirmation alert not appears'
