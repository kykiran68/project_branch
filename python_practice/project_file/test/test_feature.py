import pytest
from module.page_module_class import DummyModulePage
from data.test_data import *

@pytest.mark.usefixtures("get_driver")
class TestDummyTicketBookingWebsite:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.dmp = DummyModulePage(self.driver)
    def test_dummy_ticket_booking(self):


        #self.dmp.check_radio_button()
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
        self.dmp.enter_billing_name(billing_name)
        self.dmp.enter_billing_phone(billing_phone)
        self.dmp.enter_billing_email_address(billing_email_address)
        self.dmp.enter_billing_street_address(billing_street_address)
        self.dmp.select_billing_country(billing_country)
        self.dmp.enter_billing_postcode(billing_postcode)
        self.dmp.enter_billing_street_address1(billing_street_address1)
        self.dmp.select_most_visited_cities()
