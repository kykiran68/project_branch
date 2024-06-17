import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def multibrowser(browser):
    if browser.lower() == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
    elif browser.lower() == 'firefox':
        driver = webdriver.Firefox()
    elif browser.lower() == 'edge':
        driver = webdriver.Edge()

    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

    # get current title
    title = driver.title
    print("website title :", title)

    # get current URL of website
    current_url = driver.current_url
    print("current URL :", current_url)

    driver.find_element(By.CSS_SELECTOR, "#fromcity").send_keys("Mumbai")
    driver.find_element(By.CSS_SELECTOR, "div>input#destcity").send_keys("Kochin")

    # check element is selected or not
    email_radio_button = driver.find_element(By.ID, "eamil")
    print("email radio is selected :", email_radio_button.is_selected())
    email_radio_button.click()
    print("email radio is selected :", email_radio_button.is_selected())

    checkbox = driver.find_element(By.XPATH, "//td[text()='Mumbai']//preceding-sibling::td/input")
    print("checkbox is_displayed :", checkbox.is_displayed())
    print("checkbox is_enabled :", checkbox.is_enabled())
    print("checkbox is_selected :", checkbox.is_selected())
    checkbox.click()
    print("checkbox is_selected :", checkbox.is_selected())

    # navigate to other website
    driver.get("https://www.facebook.com/")

    # get attribute
    username_elem = driver.find_element(By.ID, "email")
    placeholder_text = username_elem.get_attribute("placeholder")
    print("placeholder text :", placeholder_text)
    print("name attribute :", username_elem.get_attribute("name"))

    time.sleep(5)
    driver.close()


multibrowser('Chrome')
