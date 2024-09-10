from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

class SeleniumCode:
    def __init__(self,driver,timeout=30):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)

    def get_element(self,locator):
        element = self.wait.until(ec.visibility_of_element_located(locator))
        return element

    def get_elements(self,locator):
        elements = self.wait.until(ec.visibility_of_element_located(locator))
        return elements

    def click_element(self,locator):
        element = self.get_element(locator)
        element.click()

    def enter_value(self,data,locator):
        element = self.get_element(locator)
        element.send_keys(data)

    def select_dropdown_value(self, value, locator):
        element = self.get_element(locator)
        obj = Select(element)
        obj.select_by_visible_text(value)
