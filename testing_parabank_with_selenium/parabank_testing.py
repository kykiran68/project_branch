import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://parabank.parasoft.com/parabank/index.htm")

###########################  LOGIN TO ACCOUNT  #################################

def login(username, password):
    user_input = driver.find_element(By.NAME, "username")
    pass_input = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Log In']")

    user_input.clear()
    pass_input.clear()

    user_input.send_keys(username)
    pass_input.send_keys(password)
    login_button.click()
    time.sleep(5)
def register(username,password):
    driver.find_element(By.XPATH,"//a[text()='Register']").click()
    driver.find_element(By.ID,"customer.firstName").send_keys("kiran")
    driver.find_element(By.ID,"customer.lastName").send_keys("Kumari")
    driver.find_element(By.ID,"customer.address.street").send_keys("RAMAMURTHY NAGAR")
    driver.find_element(By.ID,"customer.address.city").send_keys("Benguluru")
    driver.find_element(By.ID,"customer.address.state").send_keys("Karnataka")
    driver.find_element(By.ID,"customer.address.zipCode").send_keys("560001")
    driver.find_element(By.ID,"customer.phoneNumber").send_keys("1234567890")
    driver.find_element(By.ID,"customer.ssn").send_keys("012")
    driver.find_element(By.ID,"customer.username").send_keys(username)
    driver.find_element(By.ID,"customer.password").send_keys(password)
    driver.find_element(By.ID,"repeatedPassword").send_keys(password)
    driver.find_element(By.XPATH,"//input[@value='Register']").click()
    time.sleep(5)
username = "kiran123"
password = "kiran123"

try:
    # Attempt to login
    login(username, password)


except TimeoutException:
    # If login failed, register a new user
    print("Invalid username. Registering new user...")
    register(username, password)
    print("Registration complete. Logging in...")



#######################  Account services  ###############################


driver.find_element(By.XPATH,"//a[text()='Open New Account']").click()
sav =driver.find_element(By.CSS_SELECTOR,"select#type")
sav_dropdown = Select(sav)
sav_dropdown.select_by_visible_text("SAVINGS")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"input.button").click()
driver.find_element(By.CSS_SELECTOR,"a#newAccountId").click()
driver.find_element(By.XPATH,"//a[text()='Accounts Overview']").click()
driver.find_element(By.XPATH,"//a[text()='home']").click()
driver.find_element(By.XPATH,"(//a[text()='Bill Pay'])[1]").click()
driver.find_element(By.XPATH,"//input[@name='payee.name']").send_keys("kiran")
driver.find_element(By.XPATH,"//input[@name='payee.address.street']").send_keys("Ramamurthy nagar")
driver.find_element(By.XPATH,"//input[@name='payee.address.city']").send_keys("Benguluru")
driver.find_element(By.XPATH,"//input[@name='payee.address.state']").send_keys("Karnataka")
driver.find_element(By.XPATH,"//input[@name='payee.address.zipCode']").send_keys("560005")
driver.find_element(By.XPATH,"//input[@name='payee.phoneNumber']").send_keys("1234567890")
driver.find_element(By.XPATH,"//input[@name='payee.accountNumber']").send_keys("9875675855674534")
driver.find_element(By.XPATH,"//input[@name='verifyAccount']").send_keys("9875675855674534")
driver.find_element(By.XPATH,"//input[@name='amount']").send_keys("50000")
time.sleep(5)


driver.find_element(By.XPATH,"//input[@value='Send Payment']").click()

driver.find_element(By.XPATH,"//a[text()='Find Transactions']").click()
driver.find_element(By.XPATH,"//input[@id='transactionId']").send_keys("1")
driver.find_element(By.XPATH,"//button[@id='findById']").click()
driver.find_element(By.XPATH,"//a[text()='Funds Transfer Received']").click()

driver.find_element(By.XPATH, "//a[text()='Find Transactions']").click()
driver.find_element(By.XPATH,"//input[@id='transactionDate']").send_keys("01-04-2022")
driver.find_element(By.XPATH,"//button[@id='findByDate']").click()

driver.find_element(By.CSS_SELECTOR,"input#fromDate").send_keys("01-04-2022")
driver.find_element(By.CSS_SELECTOR,"input#toDate").send_keys("12-30-2024")
driver.find_element(By.CSS_SELECTOR,"button#findByDateRange").click()

driver.find_element(By.XPATH,"//a[text()='Update Contact Info']").click()
time.sleep(10)
driver.find_element(By.XPATH,"//a[text()='Request Loan']").click()
driver.find_element(By.CSS_SELECTOR,"input#amount").send_keys("1000000")
driver.find_element(By.CSS_SELECTOR,"input#downPayment").send_keys("10000")
driver.find_element(By.CSS_SELECTOR,"input.button").click()

driver.find_element(By.CSS_SELECTOR,"ul.button").click()

time.sleep(10)
driver.close()