# tests/test_cart.py
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import UnexpectedAlertPresentException
#from conftest import *
def test_add_product_to_cart(driver, login):
    time.sleep(5)
    driver.find_element(By.LINK_TEXT, "Samsung galaxy s6").click()
    time.sleep(5)  # Wait for the product page to load
    driver.find_element(By.XPATH, "//a[@onclick='addToCart(1)']").click()
    time.sleep(5)  # Wait for the alert to appear
    try:
        alert = driver.switch_to.alert
        alert.accept()
        print("Product added to cart alert accepted.")
    except UnexpectedAlertPresentException:
        pytest.fail("Unexpected alert present during adding product to cart.")
    # Verify the product is added to the cart
    driver.find_element(By.ID, "cartur").click()
    time.sleep(2)  # Wait for the cart page to load
    cart_items = driver.find_elements(By.CLASS_NAME, "success")

def test_cart_page(driver, login):
    driver.find_element(By.ID, "cartur").click()
    time.sleep(2)  # Wait for the cart page to load
    try:
        assert driver.find_element(By.ID, "tbodyid").is_displayed(), "Cart page not displayed."
        print("Cart page is displayed correctly.")
    except Exception as e:
        pytest.fail(f"Cart page verification failed: {str(e)}")
