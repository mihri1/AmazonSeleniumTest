from selenium.webdriver.common.by import By
import time
from Main.BasePage import BasePage
from Main.locators import Locators


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Locators.base_url)
        self.driver.maximize_window()
        self.click((By.NAME, Locators.close_cookie_name))

    def search(self):
        self.enter_text((By.ID, Locators.search_box_locator_id), Locators.search_box_text)
        self.click((By.ID, Locators.search_summit_button_id))
        self.click((By.CSS_SELECTOR, Locators.product))

    def get_product_info(self):
        self.click((By.XPATH, Locators.product_color))  # to get product color
        print("\n" + self.text((By.XPATH, Locators.get_color)))
        time.sleep(1)
        print("Size:" + self.text((By.XPATH, Locators.product_size)))  # to get product memory size
        time.sleep(1)
        print("Stock:" + self.text((By.XPATH, Locators.availability)))  # to get product stock
        time.sleep(1)
        print("Price:" + str(self.text((By.CSS_SELECTOR, Locators.price))) + "TL")

    def chart(self):
        self.click((By.XPATH, Locators.add_chart_button))
        time.sleep(1)
        print("Added the shopping chart!")

    def check_amount(self):
        return self.text((By.XPATH, Locators.product_amount))
