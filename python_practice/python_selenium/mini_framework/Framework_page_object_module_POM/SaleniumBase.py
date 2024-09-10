from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class selenium_base:
    def __init__(self,driver,timeout=30):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)

    def get_element(self,locator):
        element = self.wait.until(ec.visibility_of_element_located(locator))
        return element

    def click_element(self,locator):
        element  = self.get_element(locator)
        element.click()

    def  enter_value(self,data,locator):
        element  = self.get_element(locator)
        element.send_keys(data)