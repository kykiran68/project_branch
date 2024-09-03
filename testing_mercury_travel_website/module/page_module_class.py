import time

from selenium import webdriver
from .page_locator import *
from data.test_data import *
from base.selenium_base import SeleniumCode



class TechmintSmartLearningManagementSystem(SeleniumCode):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def enter_mobile_no(self, mobile_no):
        self.enter_value(mobile_no, mobile_no_locator)
        time.sleep(10)


    def click_button_otp(self):
        self.click_element(button_locator)


    def enter_otp1(self,otp1):
        self.enter_value(otp1,otp1_locator)

    def enter_otp2(self,otp2):
        self.enter_value(otp2,otp2_locator)

    def enter_otp3(self,otp3):
        self.enter_value(otp3,otp3_locator)

    def enter_otp4(self,otp4):
        self.enter_value(otp4,otp4_locator)

    def enter_otp5(self,otp5):
        self.enter_value(otp5,otp5_locator)

    def enter_otp6(self,otp6):
        self.enter_value(otp6,otp6_locator)

    def click_verify_otp(self):
        self.click_element(verify_otp_locator)

    def click_on_profile(self):
        self.click_element(profile_select_locator)

    def click_administrator(self):
        self.click_element(select_administrator_locator)

    def click_sidebar(self):
        self.click_element(goto_sidebar_locator)

    def click_view_all(self):
        self.click_element(view_all_locator)

    def click_on_school_leaving(self):
        self.click_element(select_slc_locator)

    def generate_certificate(self):
        self.click_element(generate_slc_locator)
        time.sleep(10)

    def click_generate(self):
        self.click_element(select_generate_locator)

        time.sleep(10)

    def enter_remark(self,put_remark):
        self.enter_value(put_remark,put_remark_locator)

    def click_on_button(self):
        self.click_element(click_button_locator)

    def click_download(self):
        self.click_element(click_download_locator)
