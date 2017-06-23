from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.google.com")
url = driver.current_url # to print the url
print url
assert "Google" in driver.title
title = driver.title # to get the title of page
print title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

#driver..back()

#assert "No results found." in driver.page_source
driver.close() #somehow close() method is not working, so used quit()