import os
url2 = 'https://www.google.co.in'
url = "https://www.goibibo.com/"
browser_setup = "chrome"

cur_dir = os.getcwd()

drivers_path = os.path.join(cur_dir, 'drivers')
if os.path.isdir(drivers_path):
    pass
else:
    os.mkdir(drivers_path)
chrome_driver_path = os.path.join(drivers_path, 'chromedriver.exe')
wait_time = 20