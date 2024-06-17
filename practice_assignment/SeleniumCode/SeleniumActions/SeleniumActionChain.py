import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

action = ActionChains(driver)


def hover_to_element():
    driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")
    teste_hub_element = driver.find_element(By.XPATH, "//a[contains(@href, 'testers-hub')]")
    action.move_to_element(teste_hub_element)
    action.perform()

    time.sleep(5)

    demo_site_testing_elem = driver.find_element(By.XPATH,
                                                 "//div[@class='menu-custom-main-menu-container']//span[contains(text(), 'Demo Testing Site')]")
    action.move_to_element(demo_site_testing_elem)
    action.perform()
    time.sleep(5)

    alert_box_element = driver.find_element(By.XPATH, "//div[@class='subsub_menu']//span[text()='AlertBox']")
    action.click(alert_box_element)
    action.perform()
    time.sleep(5)


def drag_and_drop_element():
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    iframe_element = driver.find_element(By.XPATH, "//iframe[@class='demo-frame lazyloaded']")
    driver.switch_to.frame(iframe_element)
    """
    first_image_element = driver.find_element(By.XPATH, "//h5[text()='High Tatras']//parent::li")
    trash_element = driver.find_element(By.ID, "trash")
    action.drag_and_drop(first_image_element, trash_element)
    action.perform()
    time.sleep(2)
    second_image_element = driver.find_element(By.XPATH, "//h5[text()='High Tatras 2']//parent::li")
    trash_element = driver.find_element(By.ID, "trash")
    action.drag_and_drop(second_image_element, trash_element)
    action.perform()

    time.sleep(2)
    third_image_element = driver.find_element(By.XPATH, "//h5[text()='High Tatras 3']//parent::li")
    trash_element = driver.find_element(By.ID, "trash")
    action.drag_and_drop(third_image_element, trash_element)
    action.perform()

    time.sleep(2)
    fourth_image_element = driver.find_element(By.XPATH, "//h5[text()='High Tatras 4']//parent::li")
    trash_element = driver.find_element(By.ID, "trash")
    action.drag_and_drop(fourth_image_element, trash_element)
    action.perform()
    """

    trash_element = driver.find_element(By.ID, "trash")
    for i in range(1, 5):
        if i == 1:
            image_element = driver.find_element(By.XPATH, "//h5[text()='High Tatras']//parent::li")
        else:
            image_element = driver.find_element(By.XPATH, f"//h5[text()='High Tatras {i}']//parent::li")
        action.drag_and_drop(image_element, trash_element)
        action.perform()
        time.sleep(2)

    time.sleep(5)


#drag_and_drop_element()
import pyautogui

print(dir(pyautogui))
def context_click_operation():
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    home_element = driver.find_element(By.XPATH, "//div[@class='menu-custom-main-menu-container']//a[text()='Home']")
    action.context_click(home_element)
    action.perform()
    time.sleep(2)
    for i in range(6):
        pyautogui.press('down')
        time.sleep(1)

    pyautogui.press('enter')
    time.sleep(10)

context_click_operation()

driver.close()
