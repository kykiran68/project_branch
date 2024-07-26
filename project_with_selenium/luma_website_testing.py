import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurations
LOGIN_URL = "https://magento.softwaretestingboard.com/customer/account/login/"
SIGNUP_URL = "https://magento.softwaretestingboard.com/customer/account/create/"
FORGOT_PASSWORD_URL = "https://magento.softwaretestingboard.com/customer/account/forgotpassword/"

USERNAME = "testuser@example.com"
PASSWORD = "TestPassword123!"
FIRST_NAME = "Test"
LAST_NAME = "User"

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://magento.softwaretestingboard.com/")

def login(driver, username, password):
    driver.get(LOGIN_URL)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    ).send_keys(username)

    driver.find_element(By.ID, "pass").send_keys(password)
    driver.find_element(By.ID, "send2").click()

    # Check for login success
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "greet"))
        )
        print("Login successful")
        return True
    except TimeoutException:
        print("Login failed")
        return False

# Perform sign-up
def signup(driver, first_name, last_name, email, password):
    driver.get(SIGNUP_URL)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "firstname"))
    ).send_keys(first_name)

    driver.find_element(By.ID, "lastname").send_keys(last_name)
    driver.find_element(By.ID, "email_address").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "password-confirmation").send_keys(password)

    driver.find_element(By.CSS_SELECTOR, "button.action.submit.primary").click()

    # Check for sign-up success
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "greet"))
        )
        print("Sign-up successful")
        return True
    except TimeoutException:
        print("Sign-up failed")
        return False

# Perform password retrieval
def forgot_password(driver, email):
    driver.get(FORGOT_PASSWORD_URL)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email_address"))
    ).send_keys(email)

    driver.find_element(By.CSS_SELECTOR, "button.action.submit.primary").click()

    # Check for password retrieval success
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "message-success success message"))
        )
        print("Password retrieval successful")
        return True
    except TimeoutException:
        print("Password retrieval failed")
        return False

# Main function to run the script

try:
    # Attempt to log in
    if not login(driver, USERNAME, PASSWORD):
        # If login fails, attempt to sign up
        if not signup(driver, FIRST_NAME, LAST_NAME, USERNAME, PASSWORD):
            # If sign-up fails, attempt to retrieve password
            forgot_password(driver, USERNAME)
finally:
    time.sleep(5)  # Wait for 5 seconds before closing the browser to observe the results
    driver.quit()

