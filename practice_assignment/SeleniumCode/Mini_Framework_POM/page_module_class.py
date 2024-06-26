from SeleniumBase import SeleniumBase
from page_locator import *

class GooglePage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def enter_value_to_search_field(self, search_value):
        self.enter_value(search_value, search_field_locator)

    def click_search_button(self):
        self.click_element(search_button_locator)
