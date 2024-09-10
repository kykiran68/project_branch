import pytest
from selenium import webdriver
from data.test_data import *



@pytest.fixture(scope='class')
def get_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.quit()