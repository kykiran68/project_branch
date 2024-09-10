import pytest

from page_module_class import GooglePage
from test_data import *
from dummy_site_page_class import DummyBookingPage

@pytest.mark.usefixtures("get_driver")
class TestGoogleSeach:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.gp = GooglePage(self.driver)
        self.db = DummyBookingPage(self.driver)

    def test_search_on_google(self):
        self.gp.enter_value_to_search_field(search_value)
        self.gp.click_search_button()

    def test_dummy_booking_website(self):
        self.db.navigate_to_dummy_booking_website()
        self.db.enter_value_billing_name_field(billing_details['Name'])
        self.db.enter_value_billing_phone(billing_details['Phone'])
        self.db.enter_value_billing_email(billing_details['email'])
        self.db.select_country_name(billing_details['country'])



