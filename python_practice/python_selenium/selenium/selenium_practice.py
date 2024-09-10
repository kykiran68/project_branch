"""
pip install selenium
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.google.co.in")
search_element = driver.find_element(By.NAME, "q")
print(search_element)
# NAME Locator
search_element.send_keys("Python Selenium")
driver.find_element(By.NAME, "btnK").click()

# LINK_TEXT, PARTIAL LINK_TEXT
tutorials_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Selenium with Python")
tutorials_link.click()

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

# Tagname Locator
header = driver.find_element(By.TAG_NAME, "h1")
print(header.text)

# ID Locator
from_city_element = driver.find_element(By.ID, "fromcity")
from_city_element.send_keys("Mumbai")

time.sleep(10)
driver.close()