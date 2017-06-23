import unittest
from selenium import webdriver
import page_objects

class Page_Objects(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        driver = self.driver
        driver.get("http://www.python.org")

    def test_pageobjects(self):
        #main_page = page_objects.(self.driver) #some error in this line
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_results_page = page_objects.SearchResultsPage(self.driver)

    def tearDown(self):
        self.driver.close();

if __name__ == "__main__":
    unittest.main()
