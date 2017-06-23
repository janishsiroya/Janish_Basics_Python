#WAIT, XPATH

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class Amazon(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login(self):
        driver = self.driver
        driver.get("https://www.amazon.com")
        elem = driver.find_element_by_id("twotabsearchtextbox")
        //elem = driver.find_element()
        elem.send_keys('iphone')
        #elem = driver.find_element_by_id("nav-orders")
        elem.send_keys(Keys.RETURN)
        #wait = WebDriverWait(driver, 30).until(EC.presence_of_element_located(By.ID, "high-price"))



        def tearDown(self):
            self.driver.close()

if __name__ == "__main__":
        unittest.main()
