from selenium.webdriver.support.select import Select
# parabank_testing_with_pytest/base/selenium_base.py
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class SeleniumCode:
    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)

    def get_element(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def get_elements(self, locator):
        return self.wait.until(ec.visibility_of_all_elements_located(locator))

    def click_element(self, locator):
        element = self.get_element(locator)
        element.click()

    def enter_value(self, value, locator):
        element = self.get_element(locator)
        element.send_keys(value)

    def select_dropdown_value(self, value, locator):
        element = self.get_element(locator)
        obj = Select(element)
        obj.select_by_visible_text(value)

    """def wait_for_element_to_be_clickable(self, locator):
        return self.wait.until(ec.element_to_be_clickable(locator))"""

    def teardown(self):
        if self.driver:
            self.driver.quit()
