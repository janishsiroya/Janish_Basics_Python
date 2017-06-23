import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class Signup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_signup(self):
        driver = self.driver
        driver.get("https://www.facebook.com")
        elem = driver.find_element_by_link_text("Sign Up")
        elem = driver.find_element_by_name("firstname")
        elem.send_keys("Janish12")
        elem = driver.find_element_by_name("lastname")
        elem.send_keys("Siroya12")
        elem = driver.find_element_by_name("reg_email__")
        elem.send_keys("janish.siroya@sjsu.edu")
        elem = driver.find_element_by_name("reg_email_confirmation__")
        elem.send_keys("janish.siroya@sjsu.edu")
        elem = driver.find_element_by_name("reg_passwd__")
        elem.send_keys("Janish123")
        select = Select(driver.find_element_by_name("birthday_month"));
        select.select_by_visible_text("Mar");
        select = Select(driver.find_element_by_name("birthday_day"));
        select.select_by_visible_text("17");
        select = Select(driver.find_element_by_name("birthday_year"));
        select.select_by_visible_text("1990");
        elem = driver.find_element_by_id("u_0_h").click();
        elem = driver.find_element_by_name("websubmit").click();
        #driver.back()

    def tearDown(self):
        self.driver.close();

if __name__ == "__main__":
    unittest.main()