from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:/Users/user/Desktop/chromedriver.exe"
service = Service(executable_path= chrome_driver_path)

options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
driver = webdriver.Chrome(options= options, service= service)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3626756864&f_AL=true&f_E=1%2C2%2C3&geoId=101620260&keywords=python%20developer&location=Israel&refresh=true")

sign_in = driver.find_element(By.LINK_TEXT, "Join now")
sign_in.click()
time.sleep(5)

email = driver.find_element(By.NAME, "email-address")
email.send_keys("sfdsf2@dff")
password = driver.find_element(By.NAME, "password")
password.send_keys("1234v3cvf")
password.send_keys(Keys.ENTER)
