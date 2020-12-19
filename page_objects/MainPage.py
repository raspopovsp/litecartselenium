from selenium.common.exceptions import NoSuchElementException

from page_objects import BasePage

accept_cookies_btn = '.btn[name=accept_cookies]'
site_menu = '#site-menu'
default_menu = '#default_menu'
categories_menu = '#default-menu > ul:nth-child(1) > li.categories.dropdown'
menu_element = '#default-menu > ul:nth-child(1) > li.categories.dropdown.open > ul > li > a'


class MainPage(BasePage):

    def accept_cookies(self):
        self.find_and_click(accept_cookies_btn)

    def navigate_to(self, category):
        self.find_and_click(categories_menu)
        menu_items = self.get_elements_list(menu_element)
        for item in menu_items:
            if category in item.text:
                item.click()
                break
            else:
                continue
