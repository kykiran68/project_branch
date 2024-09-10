"""
pip install selenium
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

driver.find_element(By.XPATH, "(//input[@id='firstname'])[1]").send_keys("Amit")
driver.find_element(By.XPATH, "(//input[@id='firstname'])[2]").send_keys("Ojha")

city_list = ["Mumbai", "Indore", "Kolkata"]
for city in city_list:
    element = driver.find_element(By.XPATH, f"//td[text()='{city}']//parent::tr//input")
    element.click()

time.sleep(10)
driver.close()


