# tests/test_signup.py
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import UnexpectedAlertPresentException
@pytest.mark.usefixtures("driver")
def test_sign_up(driver):
    driver.find_element(By.ID, "signin2").click()
    time.sleep(2)  # Wait for the sign-up modal to appear
    driver.find_element(By.ID, "sign-username").send_keys("JohnSmith")  # Replace with actual username
    driver.find_element(By.ID, "sign-password").send_keys("John12345")  # Replace with actual password
    driver.find_element(By.XPATH, "//button[@onclick='register()']").click()
    time.sleep(5)  # Wait for the alert to appear
    try:
        alert = driver.switch_to.alert
        alert.accept()
        print("Sign-up alert accepted.")
    except UnexpectedAlertPresentException:
        pytest.fail("Unexpected alert present during sign-up.")
