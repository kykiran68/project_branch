import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="class")
def get_selenium_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.co.in")
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.close()