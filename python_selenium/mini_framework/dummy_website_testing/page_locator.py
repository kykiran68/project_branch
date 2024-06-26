from selenium.webdriver.common.by import By

#radio_button_locator = (By.XPATH, "//input[@value='radio_123']")
firstname_locator = (By.XPATH, "//input[@name='firstname'][1]")
lastname_locator = (By.XPATH, "//input[@name='firstname'][2]")
dob_locator = (By.XPATH,"//input[@id='birthday']")
gender_locator = (By.XPATH,"//input[@id='female']")
additional_passengers_locator = (By.XPATH,"//select[@id='admorepass']/option [2]")
travel_locator = (By.XPATH,"//input[@id='oneway']")
from_city_locator = (By.XPATH,"//input[@name='fromcity']")
destination_city_locator = (By.XPATH,"//input[@id='destcity']")
departure_date_locator = (By.XPATH,"//input[@id='departdate']")
return_date_locator = (By.XPATH,"//input[@id='returndate']")
interview_date_locator = (By.XPATH,"//input[@id='visadate']")
receive_dummy_ticket_locator = (By.ID, "whatsapp")
billing_name_locator = (By.XPATH,"//input[@id='billing_name']")
billing_phone_locator = (By.XPATH,"//input[@id='billing_phone']")
billing_email_address_locator = (By.XPATH,"//input[@id='billing_email']")
billing_street_address_locator = (By.XPATH,"//input[@id='billing_address']")
billing_country_locator = (By.XPATH, "//select[@id='billing_country']")
billing_postcode_locator = (By.CSS_SELECTOR,"input#postcode")
billing_street_address1_locator = (By.CSS_SELECTOR,"#street_address1")
city_option_locator = (By.XPATH, "//input[@type='checkbox'][1]")
