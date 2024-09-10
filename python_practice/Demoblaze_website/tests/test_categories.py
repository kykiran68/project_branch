# tests/test_categories.py
import time
import pytest
from selenium.webdriver.common.by import By
#from fixtures.conftest import *
def test_categories(driver, login):
    categories = ["Phones", "Laptops", "Monitors"]
    for category in categories:
        driver.find_element(By.LINK_TEXT, category).click()
        time.sleep(2)  # Wait for the category page to load
        try:
            assert driver.find_element(By.ID, "tbodyid").is_displayed()
            print(f"{category} category products are displayed correctly.")
        except Exception as e:
            pytest.fail(f"{category} category verification failed: {str(e)}")
