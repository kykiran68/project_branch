# tests/test_home.py
import time
import pytest
from selenium.webdriver.common.by import By
@pytest.mark.usefixtures("driver")
def test_home_page(driver, login):
    # Verify the presence of the home page elements
    try:
        assert driver.find_element(By.ID, "nava").is_displayed()
        assert driver.find_element(By.ID, "carouselExampleIndicators").is_displayed()
        assert driver.find_element(By.ID, "cat").is_displayed()
        assert driver.find_element(By.ID, "tbodyid").is_displayed()
        print("Home page elements are displayed correctly.")
    except Exception as e:
        pytest.fail(f"Home page verification failed: {str(e)}")
