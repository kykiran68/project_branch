from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import time

# Navigate to the URL https://demo.nopcommerce.com/.
# Verify that the homepage loads without errors.

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
# Define the wait
wait = WebDriverWait(driver, 10)
driver.get("https://demo.nopcommerce.com/")


def login(username, password):
    driver.find_element(By.CSS_SELECTOR, ".ico-login").click()
    driver.find_element(By.CSS_SELECTOR, "#Email").send_keys(username)
    driver.find_element(By.CSS_SELECTOR,".password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, ".login-button").click()

login("kykiran68@gmail.com", "Kiran@123")

# Check the presence and functionality of the following navigation links:
# Home
# Computers (hover and check subcategories)
# Electronics (hover and check subcategories)
# Apparel
# Digital Downloads
# Books
# Jewelry
# Gift Cards

dropdown=driver.find_element(By.XPATH,"(//a[text()='Computers '])[1]")
webdriver.ActionChains(driver).move_to_element(dropdown).perform()

# Select "Desktops" from the dropdown menu under "Computers"
desktops_option = driver.find_element(By.XPATH, "//a[text()='Desktops ']")
desktops_option.click()

position = driver.find_element(By.ID,"products-orderby")
sel_ord = Select(position)
sel_ord.select_by_visible_text("Price: Low to High")
time.sleep(5)

dropdown=driver.find_element(By.XPATH,"(//a[text()='Computers '])[1]")
webdriver.ActionChains(driver).move_to_element(dropdown).perform()

# Select "Notebooks " from the dropdown menu under "Computers"
notebook_option = driver.find_element(By.XPATH, "//a[text()='Notebooks ']")
notebook_option.click()

position1 = driver.find_element(By.ID,"products-orderby")
sel_ord1 = Select(position1)
sel_ord1.select_by_visible_text("Price: High to Low")
#driver.find_element(By.XPATH,"(//button[text()='Add to cart'])[2]").click()
time.sleep(5)

dropdown=driver.find_element(By.XPATH,"(//a[text()='Computers '])[1]")
webdriver.ActionChains(driver).move_to_element(dropdown).perform()

# Select "Software " from the dropdown menu under "Computers"
software_option = driver.find_element(By.XPATH, "//a[text()='Software ']")
software_option.click()
driver.find_element(By.XPATH,"//a[@data-viewmode='grid']").click()

dropdown1=driver.find_element(By.XPATH,"(//a[text()='Electronics '])[1]")
webdriver.ActionChains(driver).move_to_element(dropdown1).perform()

# Select "Camera & photo " from the dropdown menu under "Electronics"
cam_option = driver.find_element(By.XPATH, "//a[text()='Camera & photo ']")
cam_option.click()

dropdown1=driver.find_element(By.XPATH,"(//a[text()='Electronics '])[1]")
webdriver.ActionChains(driver).move_to_element(dropdown1).perform()

# Select "Cell phones " from the dropdown menu under "Electronics"
cell_option = driver.find_element(By.XPATH, "//a[text()='Cell phones ']")
cell_option.click()

dropdown1=driver.find_element(By.XPATH,"(//a[text()='Electronics '])[1]")
webdriver.ActionChains(driver).move_to_element(dropdown1).perform()

# Select "Others  " from the dropdown menu under "Electronics"
oth_option = driver.find_element(By.XPATH, "//a[text()='Others ']")
oth_option.click()

dropdown2=driver.find_element(By.XPATH,"(//a[text()='Apparel '])[1]")
webdriver.ActionChains(driver).move_to_element(dropdown2).perform()

# Select "Shoes " from the dropdown menu under "Apparel "
shoe_option = driver.find_element(By.XPATH, "//a[text()='Shoes ']")
shoe_option.click()
driver.find_element(By.LINK_TEXT,"/adidas-consortium-campus-80s-running-shoes").click()
size = driver.find_element(By.ID,"select.valid")
sel_size = Select(size)
sel_size.select_by_value("22")


time.sleep(10)
driver.close()
