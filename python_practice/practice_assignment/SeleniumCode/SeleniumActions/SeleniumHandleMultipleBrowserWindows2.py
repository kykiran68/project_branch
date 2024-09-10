from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
import time
from datetime import datetime


driver = webdriver.Chrome()
driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "What is Manual Testing").click()
driver.find_element(By.LINK_TEXT, "Software Testing Principles").click()
driver.find_element(By.LINK_TEXT, "Software Testing Methods").click()
driver.find_element(By.LINK_TEXT, "Black Box Testing").click()


windows_list = driver.window_handles
print(windows_list)
for i in range(len(windows_list)):
    driver.switch_to.window(windows_list[i])
    time.sleep(5)
    driver.close()


driver.switch_to.window(windows_list[0])
time.sleep(5)



driver.close()


