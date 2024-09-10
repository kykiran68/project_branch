
from selenium.webdriver.common.by import By

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

