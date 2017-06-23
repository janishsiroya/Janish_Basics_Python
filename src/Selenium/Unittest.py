#from __future__ import absolute_import
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase): #test case class is inherited from unittest.TestCase
    #TestCase class is a way to tell unittest that it is a test case

    def setUp(self): # it is part of initialization and this method will always be called before every test function
        self.driver = webdriver.Firefox()

    def test_search(self): #test case method name should always start with test
        driver = self.driver
        driver.get("https://www.google.com")
        self.assertIn("Google", driver.title)
        title = driver.title
        print title
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


    def tearDown(self): # this method will be called after every test method. this will do cleanup of all actions
        self.driver.close()

if __name__ == "__main__": # code to run the test
        unittest.main()