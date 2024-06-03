from selenium import webdriver
from .page_locator import *
from data.test_data import *
from base.selenium_base import SeleniumCode



class DummyModulePage(SeleniumCode):
    def __init__(self, driver):
        super().__init__(driver=driver)

#    #def navigate_to_dummy_website(self):
#    #   self.driver.get(url)

#    def check_radio_button(self):
#       for ele in radio_button_locator:
#            self.click_element(ele)


    def enter_pd_first_name(self, firstname):
        self.enter_value(firstname, firstname_locator)

    def enter_pd_last_name(self, lastname):
        self.enter_value(lastname, lastname_locator)

    def enter_pd_dob(self, dob):
        self.enter_value(dob, dob_locator)

    def choose_pd_gender(self):
        self.click_element(gender_locator)

    def select_number_of_additional_passengers(self, ):
        self.click_element(additional_passengers_locator)

    def choose_travel_details(self):
        self.click_element(travel_locator)

    def enter_td_from_city(self, from_city):
        self.enter_value(from_city, from_city_locator)

    def enter_td_destination_city(self, destination_city):
        self.enter_value(destination_city, destination_city_locator)

    def enter_td_departure_date(self, departure_date):
        self.enter_value(departure_date, departure_date_locator)

    def enter_td_return_date(self, return_date):
        self.enter_value(return_date, return_date_locator)

    def enter_visa_interview_date(self, interview_date):
        self.enter_value(interview_date, interview_date_locator)

    def enter_receive_dummy_ticket(self):
        self.click_element(receive_dummy_ticket_locator)

    def enter_billing_name(self, billing_name):
        self.enter_value(billing_name, billing_name_locator)

    def enter_billing_phone(self, billing_phone):
        self.enter_value(billing_phone, billing_phone_locator)

    def enter_billing_email_address(self, billing_email_address):
        self.enter_value(billing_email_address, billing_email_address_locator)

    def enter_billing_street_address(self, billing_street_address):
        self.enter_value(billing_street_address, billing_street_address_locator)

    def select_billing_country(self, billing_country):
        self.select_dropdown_value(billing_country,billing_country_locator)

    def enter_billing_postcode(self, billing_postcode):
        self.enter_value(billing_postcode, billing_postcode_locator)

    def enter_billing_street_address1(self, billing_street_address1):
        self.enter_value(billing_street_address1, billing_street_address1_locator)

    def select_most_visited_cities(self):
        self.click_element(city_option_locator)