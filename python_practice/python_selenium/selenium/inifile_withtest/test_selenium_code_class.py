import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

@pytest.mark.usefixtures("get_selenium_driver")
class TestGoogleSearch:
    def test_google(self):
        self.driver.find_element(By.NAME,"q").send_keys("python selenium")

    def test_click(self):
        self.driver.find_element(By.NAME,"btnK").click()
        time.sleep
