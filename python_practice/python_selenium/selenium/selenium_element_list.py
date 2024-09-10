import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def multibrowser(browser):
    if browser.lower() == 'chrome':
        driver=webdriver.Chrome()
    elif browser.lower() == 'firefox':
        driver = webdriver.Firefox()
    elif browser.lower() == 'edge':
        driver = webdriver.Edge()

    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

    element_list = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    print(element_list)
    for element in element_list:
        element.click()
        time.sleep(2)

    driver.close()

multibrowser('firefox')

