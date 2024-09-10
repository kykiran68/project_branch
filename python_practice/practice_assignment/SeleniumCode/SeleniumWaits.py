"""
1. implicit wait : This wait will apply on all the element of the webpage
2. explicit wait : This wait will apply on specific element of the page.
3. Fluent wait : This wait will apply on specific element of the page with customize frequency of poll.
4. static waits : This is hard corded sleep between two steps
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


driver = webdriver.Chrome()
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.maximize_window()
#driver.implicitly_wait(10)
#wait = WebDriverWait(driver, timeout=15) # explicit wait

wait = WebDriverWait(driver, timeout=5, poll_frequency=1) # fluent wait with custom poll frequency

t1 = time.time()
try:
    element = driver.find_element(By.ID, "billing_name")
    element.send_keys("Mumbai")
except Exception as e:
    print(e)
t2 = time.time()
print("total time taken :", t2-t1)


b1 = time.time()
try:
    #element = wait.until(ec.visibility_of_element_located((By.ID, "billing_phone234")))
    element = wait.until(ec.element_to_be_clickable((By.ID, "billing_phone234")))
    print(element)
    element.send_keys("9889798789")
except Exception as e:
    print(e)
b2 = time.time()
print("total time taken :", b2-b1)

time.sleep(5) # static wait
driver.close()
