
# tests/test_checkout.py
import time
import pytest
from selenium.webdriver.common.by import By
#from fixtures.conftest import *
def test_checkout_process(driver, login):
    driver.find_element(By.ID, "cartur").click()
    time.sleep(2)  # Wait for the cart page to load
    driver.find_element(By.XPATH, "//button[@data-target='#orderModal']").click()
    time.sleep(2)  # Wait for the order modal to appear
    driver.find_element(By.ID, "name").send_keys("John Doe")
    driver.find_element(By.ID, "country").send_keys("USA")
    driver.find_element(By.ID, "city").send_keys("New York")
    driver.find_element(By.ID, "card").send_keys("1234567890123456")
    driver.find_element(By.ID, "month").send_keys("12")
    driver.find_element(By.ID, "year").send_keys("2025")
    driver.find_element(By.XPATH, "//button[@onclick='purchaseOrder()']").click()
    time.sleep(5)  # Wait for the purchase confirmation
    try:
        confirmation = driver.find_element(By.CLASS_NAME, "sweet-alert")
        assert confirmation.is_displayed()
        print("Purchase completed successfully.")
        # Additional verification for the confirmation message
        confirmation_message = driver.find_element(By.CSS_SELECTOR, ".sweet-alert").text
        assert "Thank you for your purchase!" in confirmation_message
    except Exception as e:
        pytest.fail(f"Checkout process failed: {str(e)}")
