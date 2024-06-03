import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.facebook.com/")
username = driver.find_element(By.XPATH, "//input[@data-testid='royal_email']")
username.send_keys("testuser@gmail.com")
password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
password.send_keys("Admin@12345")
login_button = driver.find_element(By.XPATH, "//button[@data-testid='royal_login_button']")
login_button.click()

incorrect_msg = driver.find_element(By.XPATH, """//div[text()="The password that you've entered is incorrect. "]""")
print(incorrect_msg.text)
assert "incorrect" in incorrect_msg.text
time.sleep(10)
driver.close()

# --------------------------------------------------------------------
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.instagram.com/")
username = driver.find_element(By.XPATH, "//input[@aria-label='Phone number, username, or email']")
username.send_keys("testuser@gmail.com")
password = driver.find_element(By.XPATH, "//input[@aria-label='Password']")
password.send_keys("Admin@12345")
login_button = driver.find_element(By.XPATH, "//button[@class=' _acan _acap _acas _aj1- _ap30']")
login_button.click()

driver.find_element(By.XPATH,"//button[@class='_a9-- _ap36 _a9_1']").click()
time.sleep(10)
driver.close()


# --------------------------------------------------------------------------------------------------------------

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://accounts.snapchat.com/accounts/v2/login")
username = driver.find_element(By.XPATH, "//input[@id='accountIdentifier']")
username.send_keys("kykiran68")
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()
password = driver.find_element(By.XPATH, "//input[@autocomplete='current-password']")
password.send_keys("Kiran@123")
login_button1 = driver.find_element(By.XPATH, "//button[@data-testid='password-submit-button']")
login_button1.click()
time.sleep(10)


# --------------------------------------------------------------------------------------------
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://brainly.in/login?entry=2&source=unlogged+homepage+header+button")
username = driver.find_element(By.XPATH, "//input[@placeholder='Username or email']")
username.send_keys("kykiran68@gmail.com")
password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
password.send_keys("Kiran@123")
login_button = driver.find_element(By.XPATH, "//button[@class='sg-button__text']")
login_button.click()


# ---------------------------------------------------------------------------------------------------------------
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("""https://in.linkedin.com/?src=go-pa&trk=sem-ga_campid.14650114788_asid.151761418307_crid.
           657403558715_kw.linkedin%20login_d.c_tid.kwd-12704335873_n.g_mt.e_geo.9302483&mcid=6844056167778418689&
           cid=&gad_source=1&gclid=CjwKCAjw88yxBhBWEiwA7cm6pUDV_e4eCvZ5zbHyttGMXW3bh_1DF_
           fsj4nc8IDQ6TG1KHP_2gBoJxoC44AQAvD_BwE&gclsrc=aw.ds""")
username = driver.find_element(By.XPATH, "//input[@autocomplete='username']")
username.send_keys("testuser@gmail.com")
password = driver.find_element(By.XPATH, "//input[@id='session_password']")
password.send_keys("Admin@12345")
login_button = driver.find_element(By.XPATH, "//button[@data-id='sign-in-form__submit-btn']")
login_button.click()
time.sleep(10)
driver.close()



# ------------------------------------------------------------------------------------------
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.pw.live/users/login")
username = driver.find_element(By.XPATH, "//input[@placeholder='test@example.com']")
username.send_keys("testuser@gmail.com")
password = driver.find_element(By.XPATH, "//input[@type='password']")
password.send_keys("Admin@12345")
login_button = driver.find_element(By.XPATH, "//input[@class='btn btn-success']")
login_button.click()
incorrect_msg = driver.find_element(By.XPATH, """//div[text()=" You are not active user. "]""")
print(incorrect_msg.text)
assert "not active" in incorrect_msg.text
time.sleep(10)
driver.close()




# ##############    Basic XPath Methods      ###############


'''1) Text Method : 
        //tagname[text()= 'text value']
        //div[text()="The password that you've entered is incorrect. "]
        //h2[text()='Facebook helps you connect and share with the people in your life.']'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.irctc.co.in/nget/train-search")
ab=driver.find_element(By.XPATH," //label[text()='INDIAN RAILWAYS']")
cd=driver.find_element(By.XPATH,"  //h2[text()='Have you not found the right one?']")
print(ab,cd)
time.sleep(10)
driver.close()


'''2) Contains Method :
        //tagname[contains(text(), 'partial value')]
        //div[contains(text(), 'incorrect')]

        //tagname[contains(@attribute, 'attribute value')]
        //button[contains(@id, 'login')]
        //*[contains(@id, 'loginb')]
        //h2[contains(text(), 'Facebook')]'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.irctc.co.in/nget/train-search")
driver.find_element(By.XPATH," //h2[contains(text(),'right one?')]")
time.sleep(10)
driver.close()


'''3) Indexing with multiple match.
                  (//input[@id='firstname'])[1]
                  (//input[@id='firstname'])[2]'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://accounts.google.com/lifecycle/steps/signup/name?continue=https://mail.google.com/mail/&dsh=S83928564:1714890470386491&flowEntry=SignUp&flowName=GlifWebSignIn&service=mail&theme=glif&TL=ALv_Gf_xKEjmg1y7wylUXLqFQRlTArbvVZjFoqzk_r0lVdbrlzZAlSlEOCeICA11")
abc=driver.find_element(By.XPATH," //input[@type='text'][1]")
abc.send_keys("kiran")
time.sleep(10)
driver.close()


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.facebook.com/r.php?api_key=124024574287414&app_id=124024574287414&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%252212m7uq8k9ft2j1jlci1tdkdtbiv46ea63bhfpk1188td11yeeywc%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26locale%3Den_US%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26response_type%3Dcode%252Cgranted_scopes%26scope%3Demail%26state%3D%257B%2522fbLoginKey%2522%253A%252212m7uq8k9ft2j1jlci1tdkdtbiv46ea63bhfpk1188td11yeeywc%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd3c2fad7-79cf-460e-99e8-70b23e783543%26tp%3Dunspecified&locale=en_GB&display=page")
abc=driver.find_element(By.XPATH," //input[@type='text'][1]").send_keys("KIRAN")

time.sleep(10)
driver.close()


'''4) Indentify element with parent reference:
                   //div[@align='left']/ul/li[3]
                   (//ul)[2]/li[3]
                   //div[@id='passContainer']/input'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.irctc.co.in/nget/train-search")
abc=driver.find_element(By.XPATH,"//div[@class='iconsection']/ul/li[2]")
abc.click()
time.sleep(10)
driver.close()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.irctc.co.in/nget/train-search")
abc=driver.find_element(By.XPATH,"//span[@class='ng-tns-c57-8 ui-autocomplete ui-widget']/input")
abc.send_keys("mumbai")
time.sleep(10)
driver.close()


'''5) AND & OR Method : //tagname[@attrb1='value' and @attrib2='value']
                     //input[@id='pass' and @name='pass']
                     //input[@value='radio_345' and @type='radio']

                     //tagname[@attrb1='value' or @attrib2='value']
                     //h1[@align='center' or  text()=' Dummy Ticket Booking Website']
                     //input[@value='radio_345' or @type='radio']'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.irctc.co.in/nget/train-search")
login_button = driver.find_element(By.XPATH, "//a[@aria-label='Click here to Login in application']")
login_button.click()
abc=driver.find_element(By.XPATH,"//input[@type='password' and @placeholder='Password']")

time.sleep(10)
driver.close()


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.irctc.co.in/nget/train-search")
abc=driver.find_element(By.XPATH,"//label[@class='heading-font' or text()=' BOOK TICKET ' ]")
print(abc)
time.sleep(10)
driver.close()


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.irctc.co.in/nget/train-search")
abc=driver.find_element(By.XPATH,"//label[@class='search_btn' or text()=' BOOK TICKET ' ]")
print(abc)
time.sleep(10)
driver.close()


############## Advance XPath Methods ##############
'''1) Following method: This method helps to identify all the element coming after the
              reference element on web page. it goes from top to bottom.

              //tagname[@attrib='value']//following::tar_tagname[@attrib='value']
              //h2[text()='Billing Details']//following::input[@id='billing_email']
              //h1[contains(text(), 'Booking Website')]//following::input[@id='male']'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.irctc.co.in/nget/train-search")
abc=driver.find_element(By.XPATH,"//label[@class='heading-font']//following::input[@role='listbox']")
print(abc)
time.sleep(10)
driver.close()


'''2) Following sibling method: This method helps to identify the younger element with help of
               elder element sibling on the web page.

               //tagname[@attrib='value']//following-sibling::tar_tagname[@attrib='value']
               //span[text()='From']//following-sibling::p[text()='Enter city or airport']
               //span[text()='To']//following-sibling::p[text()='Enter city or airport']
               //div[@align='left']//li[2]//following-sibling::li
               //table[@id='cities']//tr[4]//following-sibling::tr[1]'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.goibibo.com/")
abc=driver.find_element(By.XPATH,"//span[text()='To']//following-sibling::p[text()='Enter city or airport']")
print(abc)
time.sleep(10)
driver.close()


'''3) preceding : This methods helps to identify all the elements which are coming before the reference
                element, it follows the element bottom to top of the webpage.

                //tagname[@attrib='value']//preceding::tar_tagname[@attrib='value']
                //input[@id='street_address1']//preceding::input[@id='male']'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
abc=driver.find_element(By.XPATH,"//input[@id='street_address1']//preceding::input[@id='male']")
print(abc)
time.sleep(10)
driver.close()


'''4) preceding-sibling : This method helps to indentify the elder element with reference of younger element
                      on the webpage.

                       //tagname[@attrib='value']//preceding-sibling::tar_tagname[@attrib='value']
                       //table[@id='cities']//tr[4]//preceding-sibling::tr[1]'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
abc=driver.find_element(By.XPATH,"//table[@id='cities']//tr[4]//preceding-sibling::tr[1]")
print(abc)
time.sleep(10)
driver.close()


'''5) parent : This method helps to identify parent element of any child element
                       //tagname[@attrib='value']//parent::tar_tagname[@attrib='value']
                       //td[text()='Indore']//parent::tr'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
abc=driver.find_element(By.XPATH,"//td[text()='Indore']//parent::tr")
print(abc)
time.sleep(10)
driver.close()


'''6) Ancestor : This method helps to identify the any grandparent or great grand parent element with
              the help of child element.
              //tagname[@attrib='value']//ancestor::tar_tagname[@attrib='value']'''


