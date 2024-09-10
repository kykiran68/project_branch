# tests/test_contact.py
# tests/test_contact.py
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import UnexpectedAlertPresentException
@pytest.mark.usefixtures("driver")
def test_contact_us(driver, login):
    driver.find_element(By.LINK_TEXT, "Contact").click()
    time.sleep(2)  # Wait for the contact modal to appear
    driver.find_element(By.ID, "recipient-email").send_keys("test@example.com")
    driver.find_element(By.ID, "recipient-name").send_keys("Test User")
    driver.find_element(By.ID, "message-text").send_keys("This is a test message.")
    driver.find_element(By.XPATH, "//button[@onclick='send()']").click()
    time.sleep(5)  # Wait for the alert to appear
    try:
        alert = driver.switch_to.alert
        alert.accept()
        print("Contact us alert accepted.")
    except UnexpectedAlertPresentException:
        pytest.fail("Unexpected alert present during contact us.")
