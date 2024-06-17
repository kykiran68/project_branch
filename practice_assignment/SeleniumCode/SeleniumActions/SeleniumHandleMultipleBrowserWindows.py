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
windows_list = driver.window_handles

driver.switch_to.window(windows_list[1])

time.sleep(2)
driver.find_element(By.NAME, "q").send_keys("Python Selenium")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@title='search' and @type='submit']").click()
time.sleep(5)

driver.close()

driver.switch_to.window(windows_list[0])

time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='widget-content']//a[text()='Home']").click()

time.sleep(5)

driver.close()


