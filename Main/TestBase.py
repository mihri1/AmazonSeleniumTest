import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Main.otherPages import HomePage


class Test_Search_Base(unittest.TestCase):

    def setUp(self):  # setting up how we want to chrome to run
        ser = Service("C:\\Users\\User\\PycharmProjects\\seleniumTest2\\Drivers\\chromedriver"
                      ".exe")
        op = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=ser, options=op)
        self.driver.maximize_window()

    def tearDown(self):  # to do the cleanup after test executed
        self.driver.close()
        self.driver.quit()


class Test_Search(Test_Search_Base):

    def setUp(self):
        super().setUp()

    def test_home_page(self):
        obj1 = HomePage(self.driver)
        obj1.search()
        obj1.get_product_info()
        obj1.chart()
        amount_result = obj1.check_amount()
        self.assertIn('1', amount_result)







