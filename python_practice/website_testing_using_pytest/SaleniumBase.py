from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
class SeleniumCode:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.timeout1 = timeout
        self.wait = WebDriverWait(self.driver, self.timeout1)

    def get_element(self, locator):
        element = self.wait.until(ec.visibility_of_element_located(locator))
        return element
    def click_element(self, locator):
        element = self.get_element(locator)
        element.click()
    def enter_value(self, data, locator):
        element = self.get_element(locator)
        element.send_keys(data)

    def select_dropdown_value(self, value, locator):
        element = self.get_element(locator)
        obj = Select(element)
        obj.select_by_visible_text(value)
