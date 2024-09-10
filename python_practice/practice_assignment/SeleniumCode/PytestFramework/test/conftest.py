import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



@pytest.fixture(scope='function', autouse=True)
def setup():
    print("function Execution initiated \n")
    yield
    print("\n function Execution completed \n")


@pytest.fixture(scope='module', autouse=True)
def setup_module():
    print("Module Execution initiated \n")
    yield
    print("\n Module Execution completed \n")


@pytest.fixture(scope='session', autouse=True)
def setup_session():
    print("Session Execution initiated \n")
    yield
    print("\n Session Execution completed \n")


@pytest.fixture(scope='package', autouse=True)
def setup_package():
    print("Package Execution initiated \n")
    yield
    print("\n Package Execution completed \n")

@pytest.fixture(scope="module")
def get_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.co.in")
    driver.implicitly_wait(10)
    return driver

@pytest.fixture(scope="class")
def get_selenium_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.co.in")
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.close()
