import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Wait_Xpath(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_wait(self):
        driver = self.driver
        driver.get("https://www.facebook.com")
        elem = driver.find_element_by_xpath("//input[@name= 'email']")
        elem.send_keys("janishsiroya@yahoo.com")
        elem = driver.find_element_by_xpath("//input[@id = 'pass']")
        elem.send_keys("J@n!$#@nub#ut!")
        elem = driver.find_element_by_id("u_0_q")
        elem.send_keys(Keys.RETURN)
        wait = WebDriverWait(driver, 50)
        elem=wait.until(EC.title_is ("Facebook"))
        elem = driver.find_element_by_link_text("Messenger").click()
        elem = wait.until(EC.title_is ("Messenger"))
        wait=WebDriverWait(driver,100)
        driver.back()

    def tearDown(self):
        self.driver.close()


if "__main__" == __name__:
    unittest.main()
