# tests/test_about.py
import time
import pytest
from selenium.webdriver.common.by import By
#from conftest import *

def test_about_us(driver, login):
    driver.find_element(By.LINK_TEXT, "About us").click()
    time.sleep(2)  # Wait for the about us modal to appear
    try:
        assert driver.find_element(By.ID, "videoModalLabel").is_displayed(), "About us modal not displayed."
        print("About us modal is displayed correctly.")
    except Exception as e:
        pytest.fail(f"About us modal verification failed: {str(e)}")
