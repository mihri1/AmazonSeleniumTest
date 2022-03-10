from selenium.webdriver.support import expected_conditions as E
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(E.visibility_of_element_located(by_locator)).click()

    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(E.visibility_of_element_located(by_locator)).send_keys(text)

    def text(self, by_locator):
        return WebDriverWait(self.driver, 10).until(E.visibility_of_element_located(by_locator)).text
