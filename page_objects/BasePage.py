from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BasePage:

    def __init__(self, driver, wait=5):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait)

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
        element = None
        try:
            element = self.__find_element(selector)
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector))).click()
        except:
            NoSuchElementException(f'{element.get_attribute("class")} not found')

    def find_and_click(self, selector):
        self.__click_element(selector)

    def get_element_text(self, selector):
        text = self.__find_element(selector).text
        return text

    def get_elements_list(self, selector):
        return self.__find_elements(selector)

    def get_element_attribute(self, selector, attr):
        element = self.__find_element(selector)
        return element.get_attribute(attr)
