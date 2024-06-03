import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://accounts.teachmint.com/")
driver.find_element(By.XPATH, "//input[@id='user-input']").send_keys("0000020232")
driver.find_element(By.XPATH, "//input[@type='submit']").click()

driver.find_element(By.XPATH, "//div[@class='otp-container']/input[1]").send_keys("1")
driver.find_element(By.XPATH, "//div[@class='otp-container']/input[2]").send_keys("2")
driver.find_element(By.XPATH, "//div[@class='otp-container']/input[3]").send_keys("0")
driver.find_element(By.XPATH, "//div[@class='otp-container']/input[4]").send_keys("9")
driver.find_element(By.XPATH, "//div[@class='otp-container']/input[5]").send_keys("9")
driver.find_element(By.XPATH, "//div[@class='otp-container']/input[6]").send_keys("2")


driver.find_element(By.XPATH, "//button[@onclick='verifyOtp()']").click()


time.sleep(10)
driver.close()