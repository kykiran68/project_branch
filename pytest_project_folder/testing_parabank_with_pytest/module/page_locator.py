# parabank_testing_with_pytest/module/page_locator.py
from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    reg_button = (By.XPATH,"//a[text()='Register']")
    FIRST_NAME = (By.ID,"customer.firstName")
    LAST_NAME = (By.ID,"customer.lastName")
    ADDRESS = (By.ID,"customer.address.street")
    CITY = (By.ID,"customer.address.city")
    STATE = (By.ID,"customer.address.state")
    ZIP = (By.ID,"customer.address.zipCode")
    PHONE = (By.ID,"customer.phoneNumber")
    SSN = (By.ID,"customer.ssn")
    USERNAME = (By.ID,"customer.username")
    PASSWORD = (By.ID,"customer.password")
    con_password = (By.ID,"repeatedPassword")
    REGISTER_BUTTON = (By.XPATH,"//input[@value='Register']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".title")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error")

class LoginPageLocators:
    USERNAME_FIELD = (By.XPATH, "//input[@name='username']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Log In']")
    expected_title = (By.XPATH,"//b[text()='Welcome']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".title")

class TransferFundsPageLocators:
    TRANS_BUTTON = (By.LINK_TEXT, "Transfer Funds")
    FROM_ACCOUNT = (By.ID, "fromAccountId")  # Assuming this is a dropdown
    TO_ACCOUNT = (By.ID, "toAccountId")      # Assuming this is a dropdown
    AMOUNT = (By.CSS_SELECTOR, "input#amount")
    TRANSFER_BUTTON = (By.CSS_SELECTOR, "input.button")
    TRANSFER_STATUS = (By.XPATH, "//h1[text()='Transfer Complete!']")

class BillPayPageLocators:
    PAYEE = (By.NAME, "payee.name")
    AMOUNT = (By.NAME, "amount")
    PAY_BUTTON = (By.CSS_SELECTOR, "input[value='Send Payment']")

class LogoutPageLocators:
    LOGOUT_BUTTON = (By.LINK_TEXT, "Log Out")
