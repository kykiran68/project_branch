import pytest

from feature_page_module import GooglePage
from test_data import *

@pytest.mark.usefixtures("get_driver")
class TestGoogleSearch:
    def test_search_google(self):
        self.gp = GooglePage(self.driver)
        self.gp.value_to_search(search_value)
        self.gp.click_search_button()
