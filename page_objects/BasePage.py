from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BasePage:

    def __init__(self, driver, wait=5):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait)

    """ просмотре аттрибутов элемента. Для отладки """
    @staticmethod
    def get_element_attributes(element):
        attrs = []
        for attr in element.get_property('attributes'):
            attrs.append([attr['name'], attr['value']])
        return attrs

    def __find_element(self, selector):
        element = None
        try:
            element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        except:
            NoSuchElementException(f'{selector} not found')
        return element

    def __find_elements(self, selector):
        elements = None
        try:
            elements = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, selector)))
        except:
            NoSuchElementException(f'{selector.get_attribute("class")} not found')
        return elements

    def __click_element(self, selector):
        try:
            element = self.__find_element(selector)
            element.click()
        except:
            NoSuchElementException(f'{selector} not found')

    def find_and_click(self, selector):
        self.__click_element(selector)

    def input_fill(self, selector, value):
        element = self.__find_element(selector)
        element.click()
        element.clear()
        element.send_keys(value)

    def get_element_text(self, selector):
        return self.__find_element(selector).text

    def get_elements_list(self, selector):
        return self.__find_elements(selector)

    def get_element_attribute(self, selector, attr):
        element = self.__find_element(selector)
        return element.get_attribute(attr)
