import pytest
from selenium.webdriver.common.by import By


def test_logout(driver, login):
    # Click on the logout button
    driver.find_element(By.ID, "logout2").click()

    # Wait for the logout process to complete
    driver.implicitly_wait(5)

    # Verify that the login button is displayed, indicating successful logout
    assert driver.find_element(By.ID, "login2").is_displayed(), "Logout failed. Login button not displayed."

    print("Logout successful.")