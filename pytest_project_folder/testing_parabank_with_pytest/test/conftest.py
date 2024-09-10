
from selenium.webdriver.common.by import By
from data.test_data import *
from module.page_module_class import LoginPage
import pytest
from selenium import webdriver
from data.test_data import url


@pytest.fixture(scope='function')
def get_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)

    yield driver

    # Quit driver after each test function
    driver.quit()


@pytest.fixture(scope='function')
def logged_in_driver(get_driver):
    driver = get_driver
    login_page = LoginPage(driver)

    # Log in before running each test
    login_page.enter_username(VALID_USERNAME)
    login_page.enter_password(VALID_PASSWORD)
    login_page.click_login()

"""    # Yield the logged-in driver to the test functions
    yield driver

    # Log out after the test
    logout_page = LogoutPage(driver)
    logout_page.click_logout()"""
