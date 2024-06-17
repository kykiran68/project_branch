"""
pip install selenium
# CSS Selector :

1. ID.
    -> #fromcity
    -> input#fromcity
    -> div>input#fromcity

2. class name:
    -> .sc-12foipm-6
    -> p.sc-12foipm-6
    -> div>p.sc-12foipm-6 # dummy website testing
    -> div>p.sc-12foipm-6.erPfRs # goibibogo.com
    -> div>textarea.gLFyf # googlec.com

3. Attribute:
    -> input[id='billing_name'] # dummy website
    -> textarea[aria-label='Search'] # google.com
    -> div[jsname='VlcLAe']>center>input[value="Google Search"]

4. Substring Option:
    -> input[value^="Google"]
    -> input[id^='billing_n']
    -> input[id^='street_address']


"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

driver.find_element(By.CSS_SELECTOR, "#fromcity").send_keys("Mumbai")
driver.find_element(By.CSS_SELECTOR, "div>input#destcity").send_keys("Kochin")


time.sleep(5)
driver.close()
