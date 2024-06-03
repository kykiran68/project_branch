from SaleniumBase import selenium_base
from page_locator import *

class GooglePage(selenium_base):
    def __init__(self,driver):
        super().__init__(driver=driver)

    def value_to_search(self,search_value):
        self.enter_value(search_value,search_field_locator)

    def click_search_button(self):
        self.click_element(search_button_locator)