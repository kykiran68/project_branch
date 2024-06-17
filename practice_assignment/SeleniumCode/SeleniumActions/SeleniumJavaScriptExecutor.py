from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
import time
from datetime import datetime


driver = webdriver.Chrome()
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.maximize_window()
driver.implicitly_wait(10)

element = driver.execute_script("return document.getElementById('fromcity')")
element.send_keys("Mumbai")
time.sleep(2)
driver.execute_script("document.getElementById('oneway').click();")
time.sleep(5)

URL = driver.execute_script("return document.URL;")
print("current URL :", URL)

title = driver.execute_script("return document.title")
print("Website Title :", title)

#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

home_tab = driver.find_element(By.XPATH, "//div[@class='widget-content']//a[text()='Home']")
home_tab_link = home_tab.get_attribute("href")
driver.execute_script(f"window.open('{home_tab_link}')")
time.sleep(5)
windows = driver.window_handles
driver.switch_to.window(windows[1])

driver.find_element(By.XPATH, "//div[@class='widget-content']//a[text()='Code Practice']").click()

time.sleep(2)

driver.close()
driver.switch_to.window(windows[0])

driver.find_element(By.XPATH, "//div[@class='widget-content']//a[text()='Python Selenium']").click()

time.sleep(10)
driver.close()
