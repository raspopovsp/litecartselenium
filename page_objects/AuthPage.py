from page_objects import BasePage

login_input = 'input[name="email"]'
pass_input = 'input[name="password"]'
login_btn = 'button[name=login]'
remember_chkbx = 'input[name=remember_me]'

alert_success = 'div.alert.alert-success'

class AuthPage(BasePage):

    def fill_login(self, email):
        self.input_fill(login_input, email)

    def fill_password(self, passwd):
        self.input_fill(pass_input, passwd)

    def login_btn_click(self):
        self.find_and_click(login_btn)

    def get_alert_text(self):
        return self.get_element_text(alert_success)
