from selenium.webdriver.common.by import By

from page_objects import BasePage

form_controls = 'div.form-control'
company_name = 'input[name=company]'
tax_id = 'input[name=tax_id]'
first_name = 'input[name=firstname]'  # require
last_name = 'input[name=lastname]'  # require
address_1 = 'input[name=address1]'
address_2 = 'input[name=address2]'
postal_code = 'input[name=postcode]'
city = 'input[name=city]'
country = 'country_code'  # require
state = 'zone_code'  # require
email = '#box-create-account > form > div:nth-child(6) > div.form-group.col-xs-6.required > div > input'  # require
phone = 'input[name=phone]'
password = '#box-create-account > form > div:nth-child(7) > div:nth-child(1) > div > input'  # require
password_confirmation = 'input[name=confirmed_password]'  # require
notification_checkbox = 'input[name=newsletter]'
privacy_policy_checkbox = 'input[name=terms_agreed]'  # require
create_btn = 'button[name=create_account]'

alert = '#notices > div.alert'


class UserRegistration(BasePage):

    def get_alert_text(self):
        return self.get_element_text(alert)

    def company_name(self, value):
        self.input_fill(company_name, value)

    def tax_id(self, value):
        self.input_fill(tax_id, value)

    def first_name(self, value):
        self.input_fill(first_name, value)

    def last_name(self, value):
        self.input_fill(last_name, value)

    def address_1(self, value):
        self.input_fill(address_1, value)

    def address_2(self, value):
        self.input_fill(address_2, value)

    def postal_code(self, value):
        self.input_fill(postal_code, value)

    def city(self, value):
        self.input_fill(city, value)

    """ select """
    def country(self, option):
        self.get_select(country, option)

    """ select. active only for USA and Canada """
    def state(self, option):
        self.get_select(state, option)

    def email(self, value):
        self.input_fill(email, value)

    def phone(self, value):
        self.input_fill(phone, value)

    def password(self, value):
        self.input_fill(password, value)

    def password_confirmation(self, value):
        self.input_fill(password_confirmation, value)

    def notification_checkbox_click(self):
        self.find_and_click(notification_checkbox)

    def privacy_checkbox_click(self):
        self.find_and_click(privacy_policy_checkbox)

    def create(self):
        self.find_and_click(create_btn)

    def customer_data(self, user_params):
        self.company_name(user_params['company_name'])
        self.tax_id(user_params['tax_id'])
        self.first_name(user_params['first_name'])
        self.last_name(user_params['last_name'])
        self.address_1(user_params['address_1'])
        self.address_2(user_params['address_2'])
        self.postal_code(user_params['postal_code'])  # 4 цифры для Австралии
        self.city(user_params['city'])
        self.country(user_params['country'])  # AU for Australia
        self.state(user_params['state'])  # VIC for Victoria
        self.email(user_params['email'])
        self.phone(user_params['phone'])
        self.password(user_params['password'])
        self.password_confirmation(user_params['password_confirmation'])

    def wait_for_inputs_visible(self):
        self.wait_for_elements(form_controls)