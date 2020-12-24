from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from utilities import LogGenerator

class BasePage:

    def __init__(self, driver, wait=5):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait)

    logger = LogGenerator.loggen()

    """ Получение аттрибутов элемента. Для отладки """
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
            self.logger.info(f'element {element.get_attribute("class")} found')
        except:
            self.logger.exception(f'selector {selector} not found')
            NoSuchElementException(f'{selector} not found')
        return element

    def __find_elements(self, selector):
        elements = []
        try:
            self.logger.info(f'elements with class - {elements[0].get_attribute("class")} found')
            elements = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, selector)))
        except:
            self.logger.exception(f'selector {selector} not found')
            NoSuchElementException(f'{selector} not found')
        return elements

    def __click_element(self, selector):
        try:
            element = self.__find_element(selector)
            self.logger.info(f'element {element.get_attribute("class")} before click')
            element.click()
            self.logger.info(f'clicked')
        except:
            self.logger.exception(f'element {selector} not clicked')

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
        try:
            return element.get_attribute(attr)
        except:
            self.logger.exception(f'Cant get {attr} from {element}')
