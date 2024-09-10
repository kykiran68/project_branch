from selenium.webdriver.common.by import By


mobile_no_locator = (By.XPATH, "//input[@id='user-input']")

button_locator = (By.XPATH, "//input[@type='submit']")

otp1_locator = (By.XPATH, "//div[@class='otp-container']/input[1]")
otp2_locator = (By.XPATH, "//div[@class='otp-container']/input[2]")
otp3_locator = (By.XPATH, "//div[@class='otp-container']/input[3]")
otp4_locator = (By.XPATH, "//div[@class='otp-container']/input[4]")
otp5_locator = (By.XPATH, "//div[@class='otp-container']/input[5]")
otp6_locator = (By.XPATH, "//div[@class='otp-container']/input[6]")

verify_otp_locator = (By.XPATH, "//button[@onclick='verifyOtp()']")

profile_select_locator = (By.XPATH,"(//div[@class='profile-data-cont'])[2]")

select_administrator_locator = (By.XPATH,"//span[@data-qa='icon-administrator']")
goto_sidebar_locator = (By.XPATH,"(//a[@class='Sidebar_sidebarLink__39rXm'])[1]")

view_all_locator = (By.XPATH,"(//span[text()='View All'])[1]")

select_slc_locator = (By.XPATH,"//h6[text()='School leaving certificate']")

generate_slc_locator = (By.XPATH,"//div[text()='Generate']")

select_checkbox_locator = (By.XPATH,"(//input[@type='checkbox'])[2]")
select_generate_locator = (By.XPATH,"//div[text()='Generate']")

put_remark_locator = (By.XPATH,"//input[@placeholder='Remarks']")

click_button_locator = (By.XPATH,"(//button[@data-qa='button,disabled-false'])[2]")

click_download_locator = (By.ID,"download")

