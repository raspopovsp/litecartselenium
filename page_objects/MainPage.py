from page_objects import BasePage

accept_cookies_btn = '.btn[name=accept_cookies]'
site_menu = '#site-menu'
default_menu = '#default_menu'
categories_menu = '#default-menu > ul:nth-child(1) > li.categories.dropdown'
menu_element = '#default-menu > ul:nth-child(1) > li.categories.dropdown.open > ul > li > a'

account_menu = '#default-menu > ul.nav.navbar-nav.navbar-right > li.account.dropdown'
new_customer = '#default-menu > ul.nav.navbar-nav.navbar-right > li.account.dropdown > ul > li:nth-child(2) > a'


class MainPage(BasePage):

    ''' принять куки (поп-ап при запуске) '''
    def accept_cookies(self):
        self.find_and_click(accept_cookies_btn)

    ''' переход к пунктам меню '''
    def navigate_to(self, category):
        self.find_and_click(categories_menu)
        menu_items = self.get_elements_list(menu_element)
        for item in menu_items:
            if category in item.text:
                item.click()
                break
            else:
                continue

    ''' Проверка меню на расхлопывание '''
    def is_expanded(self):
        menu_class = self.get_element_attribute(account_menu, 'class')
        if 'open' in menu_class:
            return True
        else:
            return False

    """ Клик по меню Sign In """
    def login_menu_click(self):
        if not self.is_expanded():
            self.find_and_click(account_menu)
        else:
            return

    """ Переход к разделу создания аккаунта """
    def goto_create_customer(self):
        self.login_menu_click()
        self.find_and_click(new_customer)