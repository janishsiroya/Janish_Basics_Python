import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Practice(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search(self):
        driver = self.driver
        driver.get("https://www.facebook.com")
        elem = driver.find_element_by_name("email")
        elem.send_keys("janishsiroya@yahoo.com")
        elem = driver.find_element_by_name("pass")
        elem.send_keys("")
        elem.send_keys(Keys.RETURN) 

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
