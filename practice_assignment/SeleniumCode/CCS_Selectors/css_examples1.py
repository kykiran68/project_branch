"""
pip install selenium
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

driver.find_element(By.CSS_SELECTOR, "#fromcity").send_keys("Mumbai")
driver.find_element(By.CSS_SELECTOR, "div>input#destcity").send_keys("Kochin")


time.sleep(5)
driver.close()
