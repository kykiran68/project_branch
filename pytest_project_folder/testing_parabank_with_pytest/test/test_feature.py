# parabank_testing_with_pytest/test/test_feature.py
import time

import pytest
from data.test_data import *
from module.page_module_class import *


@pytest.mark.parametrize(
    "first_name, last_name, address, city, state, zip_code, phone, ssn, username, password,con_password",
    REGISTRATION_DATA)
def test_registration(get_driver, first_name, last_name, address, city, state, zip_code, phone, ssn, username, password,
                      con_password):
    driver = get_driver
    registration_page = RegistrationPage(driver)

    registration_page.enter_registration_details(
        first_name, last_name, address, city, state, zip_code, phone, ssn, username, password,con_password
    )


@pytest.mark.parametrize("username, password, expected_title", [
    (VALID_USERNAME, VALID_PASSWORD, "Welcome"),
    ])
def test_login(get_driver,username, password, expected_title):
    driver = get_driver
    login_page = LoginPage(driver)

    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()
    time.sleep(5)

    assert expected_title in login_page.expected_title()


@pytest.mark.parametrize("username, password, get_error_message", [
        (INVALID_USERNAME, INVALID_PASSWORD, "Error!")
])
def test_invalid_login(get_driver,username, password, get_error_message):
    driver = get_driver
    login_page = LoginPage(driver)

    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()
    time.sleep(5)

    assert get_error_message in login_page.get_error_message()


@pytest.mark.parametrize("from_account, to_account, amount, is_success", TRANSFER_DATA)
def test_transfer_funds(logged_in_driver, from_account, to_account, amount, is_success):
    driver = logged_in_driver
    transfer_page = TransferFundsPage(driver)

    transfer_page.transfer_funds(from_account, to_account, amount)

    if is_success:
        assert "Transfer Complete!" in transfer_page.get_transfer_status()
    else:
        assert "Error!" in transfer_page.get_transfer_status()


@pytest.mark.parametrize("payee, amount, is_success", BILL_PAY_DATA)
def test_pay_bill(get_driver,logged_in_driver, payee, amount, is_success):
    driver = get_driver
    bill_pay_page = BillPayPage(driver)

    bill_pay_page.pay_bill(payee, amount)

    if is_success:
        assert "Bill Payment Complete" in bill_pay_page.get_bill_payment_status()
    else:
        assert "Error" in bill_pay_page.get_bill_payment_status()


def test_logout(get_driver,logged_in_driver):
    driver = get_driver
    login_page = LoginPage(driver)

    login_page.enter_username(VALID_USERNAME)
    login_page.enter_password(VALID_PASSWORD)
    login_page.click_login()

    logout_page = LogoutPage(driver)
    logout_page.click_logout()

    assert "You have logged out" in driver.title
