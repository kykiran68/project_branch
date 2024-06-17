import time

import pytest
from selenium.webdriver.common.by import By

@pytest.mark.smoke
def test_search_on_google(get_driver):
    driver = get_driver
    driver.find_element(By.NAME, "q").send_keys("Python Selenium")
    driver.find_element(By.NAME, "btnK").click()
    time.sleep(5)
    driver.back()
    time.sleep(2)
    driver.forward()
