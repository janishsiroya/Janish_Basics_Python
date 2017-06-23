#WAIT, XPATH

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class FacebookLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login(self):
        driver = self.driver
        driver.get("https://www.facebook.com")
        #elem = driver.find_element_by_name("email")
        elem = driver.find_element_by_xpath("//input[@name='email']")
        # use of XML path
        #elem = driver.find_element_by_xpath("//form[input/@name='email']") # not working
        #elem=driver.find_element_by_xpath("//form[@id='login_form']/input[1]") # not working
        elem.send_keys("janishsiroya@yahoo.com")
        elem = driver.find_element_by_name("pass")
        elem.send_keys("")
        #elem = driver.find_element_by_id()
        elem.send_keys(Keys.RETURN)
        wait = WebDriverWait(driver,15)
        elem = wait.until(EC.title_is('Facebook'))
        elem = driver.find_element_by_link_text("Messenger").click()
        elem = wait.until(EC.title_is('Messenger'))
        #driver.implicitly_wait(10)
        driver.back()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
