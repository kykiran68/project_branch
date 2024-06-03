import pytest
from selenium import  webdriver
from test_data import *

@pytest.fixture(scope="class")
def get_driver(request):
    driver =  webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)
    request.cls.driver = driver