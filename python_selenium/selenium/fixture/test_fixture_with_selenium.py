import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



@pytest.fixture(scope="module")
def test_get_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.co.in")
    driver.implicitly_wait(10)
    return driver






