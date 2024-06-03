'''
CSS Selector :

1. ID.
    -> fromcity
    -> input#fromcity
    -> div>input#fromcity'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.railyatri.in/live-train-status")

driver.find_element(By.CSS_SELECTOR, "#from_station").send_keys("LTT")

driver.find_element(By.CSS_SELECTOR, "div>input#to_station").send_keys("Kochin")
time.sleep(10)
driver.close()


'''2. class name:
    -> .sc-12foipm-6
    -> p.sc-12foipm-6
    -> div>p.sc-12foipm-6 # dummy website testing
    -> div>p.sc-12foipm-6.erPfRs # goibibo.com
    -> div>textarea.gLFyf'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.railyatri.in/live-train-status")
driver.find_element(By.CSS_SELECTOR, "div>input.trainpicker").send_keys("02141")
button_k= driver.find_element(By.CSS_SELECTOR,"div>button.find-train-btn")
button_k.click()
time.sleep(10)
driver.close()


'''3. Attribute:
    -> input[id='billing_name'] # dummy website
    -> textarea[aria-label='Search'] # google.com
    -> div[jsname='VlcLAe']>center>input[value="Google Search"]'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.railyatri.in/live-train-status")
driver.find_element(By.CSS_SELECTOR, "input[id='from_station']").send_keys("MMR"[1])
driver.find_element(By.CSS_SELECTOR, "input[id='to_station']").send_keys("ARRAH"[1])
driver.find_element(By.CSS_SELECTOR,"button[id='station_submit']").send_keys()
time.sleep(10)
driver.close()


'''4. Substring Option:
    -> input[value^="Google"]
    -> input[id^='billing_n']
    -> input[id^='street_address']
'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.irctc.co.in/nget/train-search")
driver.find_element(By.CSS_SELECTOR, "input[aria-activedescendant^='p-highlighted']").send_keys("MMR")
driver.find_element(By.CSS_SELECTOR, "input[aria-controls='pr_id_2_list']").send_keys("ARA JN")

time.sleep(10)
driver.close()


