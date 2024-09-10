from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
from datetime import datetime


driver = webdriver.Chrome()
driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")
driver.implicitly_wait(15)
driver.maximize_window()

# Alert box
"""
driver.find_element(By.ID, "btnShowMsg").click()
time.sleep(5)
alert_obj = Alert(driver)
print(alert_obj.text)
alert_obj.accept()
time.sleep(5)
"""

# Confirm Box
"""
driver.find_element(By.ID, "button").click()
time.sleep(5)
alert_obj = Alert(driver)
print(alert_obj.text)
#alert_obj.accept()
alert_obj.dismiss()
msg = driver.find_element(By.ID, "demo")
print(msg.text)
"""


#Prompt Box
driver.find_element(By.ID, "promptbtn").click()
time.sleep(5)
alert_obj = Alert(driver)
print(alert_obj.text)
alert_obj.send_keys("GTM")
time.sleep(2)
alert_obj.accept()
#alert_obj.dismiss()
msg = driver.find_element(By.ID, "prompt")
print(msg.text)


driver.close()

