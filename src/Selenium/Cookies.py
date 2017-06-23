#from __future__ import absolute_import
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Cookies(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_cookies(self):
        driver = self.driver
        driver.get("https://www.google.com")
        self.assertIn("Google", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("dog")
        elem.send_keys(Keys.RETURN)
        cookie = {'name':'foo', 'value': 'bar'}
        driver.add_cookie(cookie)
        driver.get_cookies()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
        unittest.main()