import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    yield driver
    driver.quit()

def test_register(driver,):
    driver.find_element(By.XPATH,"//a[text()='Register']").click()
    driver.find_element(By.ID,"customer.firstName").send_keys("kiran")
    driver.find_element(By.ID,"customer.lastName").send_keys("Kumari")
    driver.find_element(By.ID,"customer.address.street").send_keys("RAMAMURTHY NAGAR")
    driver.find_element(By.ID,"customer.address.city").send_keys("Benguluru")
    driver.find_element(By.ID,"customer.address.state").send_keys("Karnataka")
    driver.find_element(By.ID,"customer.address.zipCode").send_keys("560001")
    driver.find_element(By.ID,"customer.phoneNumber").send_keys("1234567890")
    driver.find_element(By.ID,"customer.ssn").send_keys("012")
    driver.find_element(By.ID,"customer.username").send_keys("kiran")
    driver.find_element(By.ID,"customer.password").send_keys("Kiran123")
    driver.find_element(By.ID,"repeatedPassword").send_keys("Kiran123")
    driver.find_element(By.XPATH,"//input[@value='Register']").click()

@pytest.fixture()
def test_login(driver):
    driver.find_element(By.NAME, "username").send_keys("john")
    driver.find_element(By.NAME, "password").send_keys("demo")
    driver.find_element(By.XPATH, "//input[@type='submit' and @value='Log In']").click()


def test_open_new_account(driver,test_login):


    driver.find_element(By.XPATH, "//a[text()='Open New Account']").click()
    sav = driver.find_element(By.CSS_SELECTOR, "select#type")
    sav_dropdown = Select(sav)
    sav_dropdown.select_by_visible_text("SAVINGS")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.button"))).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a#newAccountId"))).click()


def test_bill_pay(driver,test_login):


    driver.find_element(By.XPATH, "//a[text()='Bill Pay']").click()
    driver.find_element(By.XPATH, "//input[@name='payee.name']").send_keys("kiran")
    driver.find_element(By.XPATH, "//input[@name='payee.address.street']").send_keys("Ramamurthy nagar")
    driver.find_element(By.XPATH, "//input[@name='payee.address.city']").send_keys("Benguluru")
    driver.find_element(By.XPATH, "//input[@name='payee.address.state']").send_keys("Karnataka")
    driver.find_element(By.XPATH, "//input[@name='payee.address.zipCode']").send_keys("560005")
    driver.find_element(By.XPATH, "//input[@name='payee.phoneNumber']").send_keys("1234567890")
    driver.find_element(By.XPATH, "//input[@name='payee.accountNumber']").send_keys("9875675855674534")
    driver.find_element(By.XPATH, "//input[@name='verifyAccount']").send_keys("9875675855674534")
    driver.find_element(By.XPATH, "//input[@name='amount']").send_keys("50000")
    driver.find_element(By.XPATH, "//input[@value='Send Payment']").click()


def test_find_transactions(driver,test_login):


    driver.find_element(By.XPATH, "//a[text()='Find Transactions']").click()
    driver.find_element(By.XPATH, "//input[@id='transactionId']").send_keys("1")
    driver.find_element(By.XPATH, "//button[@id='findById']").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Funds Transfer Received']"))).click()

    driver.find_element(By.XPATH, "//a[text()='Find Transactions']").click()
    driver.find_element(By.XPATH, "//input[@id='transactionDate']").send_keys("01-04-2022")
    driver.find_element(By.XPATH, "//button[@id='findByDate']").click()

    driver.find_element(By.CSS_SELECTOR, "input#fromDate").send_keys("01-04-2022")
    driver.find_element(By.CSS_SELECTOR, "input#toDate").send_keys("12-30-2024")
    driver.find_element(By.CSS_SELECTOR, "button#findByDateRange").click()


def test_update_contact_info(driver,test_login):


    driver.find_element(By.XPATH, "//a[text()='Update Contact Info']").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[text()='Request Loan']")))


def test_request_loan(driver,test_login):


    driver.find_element(By.XPATH, "//a[text()='Request Loan']").click()
    driver.find_element(By.CSS_SELECTOR, "input#amount").send_keys("1000000")
    driver.find_element(By.CSS_SELECTOR, "input#downPayment").send_keys("10000")
    driver.find_element(By.CSS_SELECTOR, "input.button").click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul.button"))).click()
