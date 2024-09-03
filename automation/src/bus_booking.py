from automation.src.browser_actions import BrowserAction
from automation.src.locators import *
from time import sleep

class Bus(BrowserAction):
    def __init__(self, driver):
        super().__init__(driver)

    def navigate_bus_booking_page(self):
        self.click_element(BUS_MENU_OPTION)

    def select_source_location(self,  src_location):
        self.input_text(BUS_FROM_LOCATION, src_location)
        sleep(2)
        element = self.driver.find_element_by_xpath(f"//span[text()='{src_location}']")
        element.click()

    def select_destination_location(self, dest_location):
        self.input_text(BUS_DEST_LOCATION, dest_location)
        sleep(2)
        element = self.driver.find_element_by_xpath(f"//span[text()='{dest_location}']")
        element.click()

    def select_date(self, date):
        self.click_element(BUS_TARVEL_DATE_CALENDER)
        sleep(2)
        element = self.driver.find_element_by_xpath(f"//span[text()='{date}']")
        element.click()

    def click_bus_search_button(self):
        self.click_element(BUS_SEARCH_BUTTON)

    def select_boarding_point(self, boarding_point):
        boarding_xpath = f"//p[text()='{boarding_point}']//ancestor::label/label"
        self.click_element((XPATH, boarding_xpath))

    def select_drop_point(self, dropingpoint):
        droping_point_xpath = f"//p[text()='{dropingpoint}']//ancestor::label/label"
        self.click_element((XPATH, droping_point_xpath))


    def select_bus_to_travel(self, bus_name):
        locator = f"//p[text()='{bus_name}']//ancestor::div[contains(@class, 'Srpcardstyles')][4]//span[text()='SHOW BUSES']"
        if self.verify_element_is_visible((XPATH, locator)):
            self.click_element((XPATH, locator))
        select_seat = f"//p[text()='{bus_name}']//ancestor::div[contains(@class, 'SrpActiveCardstyles')]//span[text()='SELECT SEAT']"
        self.click_element((XPATH, select_seat))

    def select_normal_seat(self, seat_num):
        seat_xpath = f"//div[contains(@class,'BusBerthstyles')]//span[text()='{seat_num}']//ancestor::div[contains(@class, 'BusSeat')]"
        self.click_element((XPATH, seat_xpath))

    def select_sleeper_seat(self, sleeper_seat):
        sleeper_seat_xpath = f"//div[contains(@class,'BusBerthstyles')]//span[text()='{sleeper_seat}']//ancestor::div[contains(@class, 'BusSleeper')]"
        self.click_element((XPATH, sleeper_seat_xpath))

    def select_passenger_seat(self, seat_type, seat_num):
        if seat_type == 'seating':
            self.select_normal_seat(seat_num)
        elif seat_type == 'sleeper':
            self.select_sleeper_seat(seat_num)

    def click_on_continue_button(self):
        self.click_element(BUS_CONTINUE_BUTTON)

    def select_passenger_gender(self, gender):
        self.select_value_from_dropdown(BUS_PASSENGER_GENDER, gender)

    def bus_enter_passenger_details(self, gender, name, age, email, phone):
        self.select_passenger_gender(gender)
        self.input_text(BUS_PASSENGER_NAME, name)
        self.input_text(BUS_PASSENGER_AGE, age)
        self.input_text(BUS_PASSENGER_EMAIL, email)
        self.input_text(BUS_PASSENGER_MOBILE, phone)

    def click_to_pay_button(self):
        self.click_element(BUS_BOOKING_PAY_BUTTON)