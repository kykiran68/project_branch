from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
import time
from datetime import datetime


driver = webdriver.Chrome()
driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")
driver.implicitly_wait(15)
driver.maximize_window()

iframe_element = driver.find_element(By.NAME, "globalSqa")
driver.switch_to.frame(iframe_element)

driver.find_element(By.XPATH, "//div[@id='mobile_menu_toggler']").click()

driver.switch_to.default_content()

page_heading = driver.find_element(By.XPATH, "//div[@class='page_heading']/h1")
print(page_heading.text)

home_page = driver.find_element(By.XPATH, "//a[text()='Home']")
home_page.click()

time.sleep(5)

driver.close()

