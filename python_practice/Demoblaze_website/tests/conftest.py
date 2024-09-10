
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import UnexpectedAlertPresentException
import time

@pytest.fixture(autouse=True)
def driver():

    driver = webdriver.Chrome()  # Ensure you have the ChromeDriver installed and in PATH
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.demoblaze.com/index.html")

    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def login(driver):
    driver.find_element(By.ID, "login2").click()
    time.sleep(2)  # Wait for the login modal to appear
    driver.find_element(By.ID, "loginusername").send_keys("Demo")
    driver.find_element(By.ID, "loginpassword").send_keys("demo")
    driver.find_element(By.XPATH, "//button[@onclick='logIn()']").click()
    time.sleep(5)  # Wait for the login to process
