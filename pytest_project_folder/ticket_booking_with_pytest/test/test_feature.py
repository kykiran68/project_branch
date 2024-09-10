import time

import pytest
from module.page_module_class import DummyModulePage
from data.test_data import *
from module.page_locator import *  # Import locators here

@pytest.mark.usefixtures("get_driver")
class TestDummyTicketBookingWebsite:

    @pytest.fixture(autouse=True)
    def setup(self, get_driver):
        self.driver = get_driver
        self.dmp = DummyModulePage(self.driver)

    def test_valid_ticket_booking(self):
        """Positive Test Case: Verify successful ticket booking with valid data."""
        self.dmp.enter_pd_first_name(firstname)
        self.dmp.enter_pd_last_name(lastname)
        self.dmp.enter_pd_dob(dob)
        self.dmp.choose_pd_gender()
        self.dmp.select_number_of_additional_passengers()
        self.dmp.choose_travel_details()
        self.dmp.enter_td_from_city(from_city)
        self.dmp.enter_td_destination_city(destination_city)
        self.dmp.enter_td_departure_date(departure_date)
        self.dmp.enter_td_return_date(return_date)
        self.dmp.enter_visa_interview_date(interview_date)
        self.dmp.enter_receive_dummy_ticket()

    def teardown_method(self, method):
        self.driver.quit()

    def test_valid_first_name(self):
        self.dmp.enter_pd_first_name(firstname)
        assert self.driver.find_element(*firstname_locator).get_attribute('value') == firstname

    def test_empty_first_name(self):
        self.dmp.enter_pd_first_name("")
        self.dmp.enter_receive_dummy_ticket()
        # Check for error message related to first name

    def test_valid_last_name(self):
        self.dmp.enter_pd_last_name(lastname)
        assert self.driver.find_element(*lastname_locator).get_attribute('value') == lastname

    def test_empty_last_name(self):
        self.dmp.enter_pd_last_name("")
        self.dmp.enter_receive_dummy_ticket()
        # Check for error message related to last name

    def test_valid_dob(self):
        self.dmp.enter_pd_dob(dob)
        self.driver.find_element(*dob_locator)

    def test_invalid_dob(self):
        self.dmp.enter_pd_dob("Invalid Date")
        time.sleep(5)
        self.dmp.enter_receive_dummy_ticket()
        # Check for error message related to invalid date

    def test_valid_gender_selection(self):
        self.dmp.choose_pd_gender()
        # Verify that gender is selected

    def test_valid_from_city(self):
        self.dmp.enter_td_from_city(from_city)
        assert self.driver.find_element(*from_city_locator).get_attribute('value') == from_city

    def test_valid_destination_city(self):
        self.dmp.enter_td_destination_city(destination_city)
        assert self.driver.find_element(*destination_city_locator).get_attribute('value') == destination_city

    def test_valid_departure_date(self):
        self.dmp.enter_td_departure_date(departure_date)
        assert self.driver.find_element(*departure_date_locator)

    def test_valid_return_date(self):
        self.dmp.enter_td_return_date(return_date)
        assert self.driver.find_element(*return_date_locator).get_attribute('value')

    def test_valid_interview_date(self):
        self.dmp.enter_visa_interview_date(interview_date)
        assert self.driver.find_element(*interview_date_locator).get_attribute('value')

    def test_valid_billing_name(self):
        self.dmp.enter_billing_name(billing_name)
        assert self.driver.find_element(*billing_name_locator).get_attribute('value') == billing_name

    def test_valid_billing_phone(self):
        self.dmp.enter_billing_phone(billing_phone)
        assert self.driver.find_element(*billing_phone_locator).get_attribute('value') == billing_phone

    def test_valid_billing_email(self):
        self.dmp.enter_billing_email_address(billing_email_address)
        assert self.driver.find_element(*billing_email_address_locator).get_attribute('value') == billing_email_address

    def test_valid_billing_street_address(self):
        self.dmp.enter_billing_street_address(billing_street_address)
        assert self.driver.find_element(*billing_street_address_locator).get_attribute('value') == billing_street_address

    def test_valid_billing_country(self):
        self.dmp.select_billing_country(billing_country)
        # Add logic to verify country selection

    def test_valid_billing_postcode(self):
        self.dmp.enter_billing_postcode(billing_postcode)
        assert self.driver.find_element(*billing_postcode_locator).get_attribute('value') == billing_postcode

    def test_valid_billing_street_address1(self):
        self.dmp.enter_billing_street_address1(billing_street_address1)
        assert self.driver.find_element(*billing_street_address1_locator).get_attribute('value') == billing_street_address1

    def test_select_most_visited_cities(self):
        self.dmp.select_most_visited_cities()
        # Add logic to verify city selection
