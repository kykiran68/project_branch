import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from _datetime import datetime
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")


def choosing_option():
    opt=driver.find_elements(By.XPATH,"//li/input[@type='radio']")
    for ele in opt:
        ele.click()

choosing_option()
driver.find_element(By.XPATH,"//input[@name='firstname'][1]").send_keys("KIRAN")
driver.find_element(By.XPATH,"//input[@name='firstname'][2]").send_keys("YADAV")
driver.find_element(By.XPATH,"//input[@id='birthday']").send_keys("01-04-2000")
driver.find_element(By.XPATH,"//input[@id='female']").click()
driver.find_element(By.XPATH,"//select[@id='admorepass']/option [2]").click()
driver.find_element(By.XPATH,"//input[@id='oneway']").click()
driver.find_element(By.XPATH,"//input[@name='fromcity']").send_keys("MUMBAI")
driver.find_element(By.XPATH,"//input[@id='destcity']").send_keys("Bengaluru")
driver.find_element(By.XPATH,"//input[@id='departdate']").send_keys(datetime.now().strftime("%d_%m_%Y"))
driver.find_element(By.XPATH,"//input[@id='returndate']").send_keys("25-05-2024")
driver.find_element(By.XPATH,"//input[@id='visadate']").send_keys("28-05-2024")
#driver.find_element(By.XPATH,"//span[text()='Both']").click()
driver.find_element(By.XPATH,"//input[@id='billing_name']").send_keys("Kiran Yadav")
driver.find_element(By.XPATH,"//input[@id='billing_phone']").send_keys("9284933477")
driver.find_element(By.XPATH,"//input[@id='billing_email']").send_keys("kykiran68@gmail.com")
driver.find_element(By.XPATH,"//input[@id='billing_address']").send_keys("Ramamurthi Nagar")
#driver.find_element(By.XPATH,"//select[@id='billing_country']/option[13]").click()
dropdown=driver.find_element(By.ID,'billing_country')
sel_obj= Select(dropdown)
sel_obj.select_by_visible_text("India")
dropdown.screenshot("element_name.png")
driver.save_screenshot("website.png")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"input#postcode").send_keys("423104")
driver.find_element(By.CSS_SELECTOR,"#Prefecture").send_keys("91")
driver.find_element(By.CSS_SELECTOR,"#street_address1").send_keys("ramammurthy nagar")
driver.find_element(By.CSS_SELECTOR,"#street_address2").send_keys("Bengaluru")
city_list = ["Mumbai", "Indore", "Kolkata", "Hyderabad", "Delhi"]
for city in city_list:
    element = driver.find_element(By.XPATH, f"//td[text()='{city}']//parent::tr//input")
    element.click()
    driver.save_screenshot("dummy_website.png")
driver.find_element(By.XPATH,"//a[text()='loop']").click()
driver.find_element(By.XPATH,"//a[text()='onlinetraining']").click()
driver.find_element(By.XPATH,"//a[text()='pytestframework']").click()
driver.find_element(By.XPATH,"//a[text()='python']").click()

time.sleep(10)
driver.close()
