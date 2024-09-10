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
driver.find_element(By.NAME, "q").send_keys("Python Selenium")
driver.find_element(By.NAME, "btnK").click()

time.sleep(10)
driver.close()