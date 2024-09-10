import time

import pytest
from selenium.webdriver.common.by import By



@pytest.mark.usefixtures("get_selenium_driver")
class TestGoogleSearch:

    def test_search_on_google(self):
        self.driver.find_element(By.NAME, "q").send_keys("Python Selenium")

    def test_click_search_button(self):
        self.driver.find_element(By.NAME, "btnK").click()
        time.sleep(5)

    def test_a3(self):
        assert 30*50 == 1500

    def test_a4(self):
        assert 300 == 100
