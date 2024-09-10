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

    driver.get("https://collegedunia.com/engineering/indore-colleges")

    element_list = driver.find_elements(By.XPATH, "//table[contains(@class, 'listing-table')]//tr//td[2]//div[contains(@class, 'clg-column')]/a")
    print(element_list)
    count = 1
    for element in element_list:
        print("College number :", count)
        print("college link :", element.get_attribute("href"))
        print("College Name :", element.get_attribute("data-csm-title"))
        print("_"*50)
        count += 1

    driver.close()



multibrowser('Chrome')
