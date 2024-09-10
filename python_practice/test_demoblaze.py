import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import UnexpectedAlertPresentException
import time

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()  # Ensure you have the ChromeDriver installed and in PATH
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.demoblaze.com/index.html")
    yield driver
    driver.quit()
@pytest.fixture()
def login(driver):
    driver.find_element(By.ID, "login2").click()
    time.sleep(2)  # Wait for the login modal to appear
    driver.find_element(By.ID, "loginusername").send_keys("Demo")
    driver.find_element(By.ID, "loginpassword").send_keys("demo")
    driver.find_element(By.XPATH, "//button[@onclick='logIn()']").click()
    time.sleep(5)  # Wait for the login to process

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

def test_login(driver,login):
    time.sleep(5)
    try:
        assert driver.find_element(By.ID, "nameofuser").is_displayed()
    except Exception as e:
        pytest.fail(f"Login failed: {str(e)}")

def test_home_page(driver,login):
    # Verify the presence of the home page elements
    try:
        assert driver.find_element(By.ID, "nava").is_displayed()
        assert driver.find_element(By.ID, "carouselExampleIndicators").is_displayed()
        assert driver.find_element(By.ID, "cat").is_displayed()
        assert driver.find_element(By.ID, "tbodyid").is_displayed()
        print("Home page elements are displayed correctly.")
    except Exception as e:
        pytest.fail(f"Home page verification failed: {str(e)}")

def test_categories(driver,login):
    categories = ["Phones", "Laptops", "Monitors"]
    for category in categories:
        driver.find_element(By.LINK_TEXT, category).click()
        time.sleep(2)  # Wait for the category page to load
        try:
            assert driver.find_element(By.ID, "tbodyid").is_displayed()
            print(f"{category} category products are displayed correctly.")
        except Exception as e:
            pytest.fail(f"{category} category verification failed: {str(e)}")

def test_add_product_to_cart(driver,login):
    #login(driver, "Demo", "demo")  # Ensure the user is logged in
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


def test_checkout_process(driver,login):

    driver.find_element(By.ID,"cartur").click()
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

def test_contact_us(driver,login):
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

def test_about_us(driver,login):
    driver.find_element(By.LINK_TEXT, "About us").click()
    time.sleep(2)  # Wait for the about us modal to appear
    try:
        assert driver.find_element(By.ID, "videoModalLabel").is_displayed(), "About us modal not displayed."
        print("About us modal is displayed correctly.")
    except Exception as e:
        pytest.fail(f"About us modal verification failed: {str(e)}")

def test_cart_page(driver,login):
    driver.find_element(By.ID, "cartur").click()
    time.sleep(2)  # Wait for the cart page to load
    try:
        assert driver.find_element(By.ID, "tbodyid").is_displayed(), "Cart page not displayed."
        print("Cart page is displayed correctly.")
    except Exception as e:
        pytest.fail(f"Cart page verification failed: {str(e)}")

def test_logout(driver,login):

    driver.find_element(By.ID, "logout2").click()
    time.sleep(2)  # Wait for the logout to process
    try:
        assert driver.find_element(By.ID, "login2").is_displayed(), "Logout failed."
        print("Logout successful.")
    except Exception as e:
        pytest.fail(f"Logout verification failed: {str(e)}")
