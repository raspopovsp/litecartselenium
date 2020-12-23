from page_objects import BasePage

login_input = 'input[name="email"]'
pass_input = 'input[name="password"]'
login_btn = 'button[name=login]'
remember_me = 'input[name=remember_me]'

alert = '#notices > div.alert'
# alert_success = 'div.alert.alert-success'
# alert_danger = 'div.alert.alert-danger'

class AuthPage(BasePage):

    def fill_login(self, email):
        self.input_fill(login_input, email)

    def fill_password(self, password):
        self.input_fill(pass_input, password)

    def login_btn_click(self):
        self.find_and_click(login_btn)

    def remember_me_check(self):
        self.find_and_click(remember_me)

    def get_alert_text(self):
        return self.get_element_text(alert)

    # def get_alert_success_text(self):
    #     return self.get_element_text(alert_success)
    #
    # def get_alert_danger_text(self):
    #     return self.get_element_text(alert_danger)
    #
