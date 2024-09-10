from automation.test_data.env import *
from automation.test_data.variables import *
from time import sleep
from automation.test_data.variables import *
import pytest

# def test_search_on_google(setup):
#     setup.launch_url(url)
#     setup.g_obj.search_data_on_google(google_search_data)
#     sleep(10)

def test_search_flight(setup):
    sleep(5)
    setup.f_obj.select_source_location(source_location)
    sleep(5)
    setup.f_obj.select_destination_location(destination_location)
    sleep(5)
    setup.f_obj.select_depart_date()
    setup.f_obj.select_return_date()
    sleep(5)
    setup.f_obj.select_number_of_travellers(adult=adults)
    sleep(5)
    setup.f_obj.click_on_search_button()
    sleep(10)
    setup.f_obj.select_maxprice_flight_for_depart()
    sleep(10)
    setup.f_obj.select_maxprice_flight_for_return()
    sleep(10)
    setup.f_obj.click_on_book_button()
    sleep(10)


@pytest.mark.bus
def test_search_bus(setup):
    setup.bus_obj.navigate_bus_booking_page()
    setup.bus_obj.select_source_location(src_location=bus_source_location)
    setup.bus_obj.select_destination_location(dest_location=bus_dest_location)
    setup.bus_obj.click_bus_search_button()
    sleep(5)
    setup.bus_obj.select_bus_to_travel(bus_name=bus_name_travel)
    sleep(5)
    setup.bus_obj.select_boarding_point(bus_boarding_point)
    sleep(2)
    setup.bus_obj.select_drop_point(bus_droping_point)
    sleep(2)
    setup.bus_obj.select_passenger_seat(seat_type, bus_passenger_seat)
    sleep(2)
    setup.bus_obj.click_on_continue_button()
    sleep(5)
    setup.bus_obj.bus_enter_passenger_details(bus_passenger_gender, bus_passenger_name, bus_passenger_age, bus_passenger_email, bus_passenger_phone)
    setup.bus_obj.click_to_pay_button()
    sleep(10)