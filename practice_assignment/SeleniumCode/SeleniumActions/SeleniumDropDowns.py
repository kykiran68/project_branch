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

driver.find_element(By.ID, "birthday").send_keys("05/05/1919")

pass_dd = driver.find_element(By.ID, "admorepass")
select_obj2 = Select(pass_dd)
select_obj2.select_by_visible_text("Add 2 more passenger (200%)")



country_dropdown = driver.find_element(By.ID, "billing_country")
select_obj = Select(country_dropdown)
# select_obj.select_by_visible_text("Bangladesh")
# select_obj.select_by_index(0) # we can select value as per index position, index starts from zero
select_obj.select_by_value("BE")




time.sleep(10)
driver.close()
