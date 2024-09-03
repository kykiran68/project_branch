from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Start the WebDriver and open the login page
driver = webdriver.Chrome()
driver.get('https://www.mercurytravels.co.in/')

# Find and click on the login button
login_button = driver.find_element(By.ID,'loginButton')
login_button.click()

# Find the login form elements and input the credentials
username_input = driver.find_element(By.ID,'emailId')
password_input = driver.find_element(By.ID,'pwd')

username_input.send_keys('your_username')
password_input.send_keys('your_password')

# Submit the form
password_input.send_keys(Keys.RETURN)

# Check if the user is not registered by looking for an error message or element
error_message = driver.find_elements_by_class_name('alert-danger')
if error_message:
    sign_up_link = driver.find_element_by_link_text('Sign Up')
    sign_up_link.click()
else:
    # Check if the password is wrong and navigate to the forgot password page
    forgot_password_link = driver.find_element_by_link_text('Forgot password?')
    forgot_password_link.click()

# Close the WebDriver
driver.quit()
