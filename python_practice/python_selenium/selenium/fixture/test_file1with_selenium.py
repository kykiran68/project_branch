import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#@pytest.mark.smoke
def google(get_driver):
    driver = get_driver
    driver.find_element(By.NAME,"q").send_keys("python selenium")
    driver.find_element(By.NAME,"btnK").click()
    time.sleep(5)

