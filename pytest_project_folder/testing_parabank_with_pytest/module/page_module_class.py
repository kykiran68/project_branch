# parabank_testing_with_pytest/module/page_module_class.py
from base.selenium_base import SeleniumCode
from module.page_locator import *
from selenium.webdriver.support.select import Select


class RegistrationPage(SeleniumCode):
    def enter_registration_details(self, first_name, last_name, address, city, state, zip_code, phone, ssn, username, password,con_password):
        self.click_element(RegistrationPageLocators.reg_button)
        self.enter_value(first_name, RegistrationPageLocators.FIRST_NAME)
        self.enter_value(last_name, RegistrationPageLocators.LAST_NAME)
        self.enter_value(address, RegistrationPageLocators.ADDRESS)
        self.enter_value(city, RegistrationPageLocators.CITY)
        self.enter_value(state, RegistrationPageLocators.STATE)
        self.enter_value(zip_code, RegistrationPageLocators.ZIP)
        self.enter_value(phone, RegistrationPageLocators.PHONE)
        self.enter_value(ssn, RegistrationPageLocators.SSN)
        self.enter_value(username, RegistrationPageLocators.USERNAME)
        self.enter_value(password, RegistrationPageLocators.PASSWORD)
        self.enter_value(con_password, RegistrationPageLocators.con_password)
        self.click_element(RegistrationPageLocators.REGISTER_BUTTON)

    def get_success_message(self):
        return self.get_element(RegistrationPageLocators.SUCCESS_MESSAGE).text

    def get_error_message(self):
        return self.get_element(RegistrationPageLocators.ERROR_MESSAGE).text

class LoginPage(SeleniumCode):
    def enter_username(self, username):
        self.enter_value(username, LoginPageLocators.USERNAME_FIELD)

    def enter_password(self, password):
        self.enter_value(password, LoginPageLocators.PASSWORD_FIELD)

    def click_login(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_element(LoginPageLocators.ERROR_MESSAGE).text

    def expected_title(self):
        return self.get_element(LoginPageLocators.expected_title).text


class TransferFundsPage(SeleniumCode):
    def transfer_funds(self, from_account, to_account, amount):
        # Click the Transfer Funds link
        self.click_element(TransferFundsPageLocators.TRANS_BUTTON)

        # Select from account from dropdown
        from_account_select = Select(self.get_element(TransferFundsPageLocators.FROM_ACCOUNT))
        from_account_select.select_by_visible_text(from_account)

        # Select to account from dropdown
        to_account_select = Select(self.get_element(TransferFundsPageLocators.TO_ACCOUNT))
        to_account_select.select_by_visible_text(to_account)

        # Enter amount
        self.enter_value(amount, TransferFundsPageLocators.AMOUNT)

        # Click Transfer button
        self.click_element(TransferFundsPageLocators.TRANSFER_BUTTON)

    def get_transfer_status(self):
        # Implement this method to retrieve transfer status
        # For example, you might look for a confirmation message
        return self.get_element(TransferFundsPageLocators.TRANSFER_STATUS).text

class BillPayPage(SeleniumCode):
    def pay_bill(self, payee, amount):
        self.enter_value(payee, BillPayPageLocators.PAYEE)
        self.enter_value(amount, BillPayPageLocators.AMOUNT)
        self.click_element(BillPayPageLocators.PAY_BUTTON)

    def get_bill_payment_status(self):
        # Implement method to get bill payment status
        pass

class LogoutPage(SeleniumCode):
    def click_logout(self):
        self.click_element(LogoutPageLocators.LOGOUT_BUTTON)
