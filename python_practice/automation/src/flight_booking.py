from .browser_actions import BrowserAction
from .locators import *

class flight(BrowserAction):
    def __init__(self, driver):
        super().__init__(driver)

    def select_source_location(self, from_location):
        #import pdb;pdb.set_trace()
        self.input_text(SRC_FLIGHT_SEARCH, from_location)
        all_datalist = self.get_list_of_elements(SRC_SEARCH_ELEMENTS)
        for element in all_datalist:
            elem_text = element.text
            target = elem_text.split("\n")[0]
            if from_location == target:
                element.click()
                break
            else:
                continue

    def select_destination_location(self, destination_location):
        self.input_text(DEST_FLIGHT_SEARCH, destination_location)
        all_datalist = self.get_list_of_elements(SRC_SEARCH_ELEMENTS)
        for element in all_datalist:
            elem_text = element.text
            target = elem_text.split("\n")[0]
            if destination_location == target:
                element.click()
                break
            else:
                continue

    def select_depart_date(self):
        self.click_element(DEPART_BOOKING_DATE)

    def select_return_date(self):
        self.click_element(RETURN_DATE_CALENDER)
        self.click_element(RETURN_BOOKING_DATE)

    def select_number_of_travellers(self, adult=None, children=None, infant=None, travel_class=None):
        self.click_element(PASSENGER_DETAILS)
        if adult is not None:
            self.input_text(ADULT_BOX, adult)
        else:
            pass

        if children is not None:
            self.input_text(CHILD_BOX, children)
        else:
            pass

        if infant is not None:
            self.input_text(INFANT_BOX, infant)
        else:
            pass

        if travel_class is not None:
            self.select_value_from_dropdown(TRAVEL_CLASS_DROPDOWN, travel_class)
        else:
            pass

    def click_on_search_button(self):
        self.click_element(SEARCH_BUTTON)


    def select_maxprice_flight_for_depart(self):
        allprices = self.get_list_of_elements(DEPART_FLIGHT_PRICES)
        price_list = []
        target_list = []
        radio_button = "//div[@class='fltHpyOnwrdWrp']//span[text()='price']//ancestor::div[@class='dF alignItemsEnd']//label"
        for price in allprices:
            print(price.text)
            data = (price.text).replace(',', "")
            price_list.append(int(data))
            target_list.append(price.text)

        min_price = max(price_list)
        min_index = price_list.index(min_price)
        target = target_list[min_index]

        print("Max Price :", min_price, target)

        target_element = radio_button.replace('price', target)
        print(target_element)
        self.click_element((XPATH, target_element))

    def select_maxprice_flight_for_return(self):
        allprices = self.get_list_of_elements(RETUNR_FLIGHT_PRICES)
        price_list = []
        target_list = []
        radio_button = "//div[@class='fltHpyRtrnWrp']//span[text()='price']//ancestor::div[@class='dF alignItemsEnd']//label"
        for price in allprices:
            print(price.text)
            data = (price.text).replace(',', "")
            price_list.append(int(data))
            target_list.append(price.text)

        min_price = max(price_list)
        min_index = price_list.index(min_price)
        target = target_list[min_index]

        print("Max Price :", min_price, target)

        target_element = radio_button.replace('price', target)
        print(target_element)
        self.click_element((XPATH, target_element))

    def click_on_book_button(self):
        self.click_element(BOOK_BUTTON)