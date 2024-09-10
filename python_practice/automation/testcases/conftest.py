import pytest
from selenium import webdriver
from automation.test_data.env import *
from automation.src.common import common

@pytest.fixture(scope='class')
def get_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    request.cls.driver = driver