from SeleniumBase import SeleniumBase
from dummy_booking_page_locator import *
from test_data import *


class DummyBookingPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def navigate_to_dummy_booking_website(self):
        self.driver.get(dummy_web_site_url)

    def enter_value_billing_name_field(self, billing_name):
        self.enter_value(billing_name, billing_name_field_locator)

    def enter_value_billing_phone(self, phone):
        self.enter_value(phone, billing_phone_field_locator)

    def enter_value_billing_email(self, email):
        self.enter_value(email, billing_email_field_locator)

    def select_country_name(self, country_name):
        self.select_dropdown_value(country_name, country_dropdown_locator)
