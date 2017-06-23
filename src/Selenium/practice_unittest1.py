import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Practice(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_janish1(self):
        driver = self.driver
        driver.get("https://www.google.com")
        self.assertIn ("Google", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("salman khan")
        elem.send_keys(Keys.RETURN)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()



