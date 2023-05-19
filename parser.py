from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options as options

s = Service('geckodriver.exe')
# url = "https://yahoo.com"
url = "https://prombez24.com/ticket/ordered/?testId=247&page=0&size=128"
# options = Options()

option = webdriver.FirefoxOptions()
new_driver_path = 'geckodriver.exe'
new_binary_path = 'C:\Program Files\Mozilla Firefox/firefox.exe'
# ops = options()
option.binary_location = new_binary_path
serv = Service(new_driver_path)

# options.binary_location = r"C:\Program Files\Mozilla Firefox/firefox.exe"
driver = webdriver.Firefox(service=serv, options=option)
driver.get(url)
button = driver.find_elements(By.CLASS_NAME, "btn btn-primary")
button.click()
