# tests/test_login.py
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import UnexpectedAlertPresentException
@pytest.mark.usefixtures("driver")
def test_login(driver, login):
    time.sleep(5)
    try:
        assert driver.find_element(By.ID, "nameofuser").is_displayed()
    except Exception as e:
        pytest.fail(f"Login failed: {str(e)}")

def test_logout(driver, login):
    driver.find_element(By.ID, "logout2").click()
    time.sleep(2)  # Wait for the logout to process
    try:
        assert driver.find_element(By.ID, "login2").is_displayed(), "Logout failed."
        print("Logout successful.")
    except Exception as e:
        pytest.fail(f"Logout verification failed: {str(e)}")
