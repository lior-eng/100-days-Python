from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

EMAIL = "0526134041"
PASSWORD = "Aa123123123"

chrome_driver_path = "C:/Users/user/Desktop/chromedriver.exe"
service = Service(executable_path= chrome_driver_path)

options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--ignore-ssl-errors')
# options.add_argument('--acceptInsecureCerts')

driver = webdriver.Chrome(options= options, service= service)
driver.get("http://www.tinder.com")
time.sleep(5)

base_window = driver.window_handles[0]
# print(driver.title)

button_login = driver.find_element(By.LINK_TEXT, "Log in")
button_login.click()
time.sleep(2)

fb_button = driver.find_element(By.XPATH, '//*[@id="u-1238065328"]/main/div[1]/div/div[1]\
                                            /div/div/div[2]/div[2]/span/div[2]/button')
fb_button.click()
time.sleep(2)

fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

email = driver.find_element(By.XPATH, '//*[@id="email"]')
email.send_keys(EMAIL)
time.sleep(1)

password = driver.find_element(By.XPATH, '//*[@id="pass"]')
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)
time.sleep(5)

driver.switch_to.window(base_window)
time.sleep(5)

allow_location = driver.find_element(By.XPATH, '//*[@id="u-1238065328"]/main/div[1]/div/div/div[3]/button[1]')
allow_location.click()
time.sleep(2)

disallow_notifications = driver.find_element(By.XPATH, '//*[@id="u-1238065328"]/main/div[1]/div/div/div[3]/button[2]')
disallow_notifications.click()
time.sleep(2)

reject_to_see_likes = driver.find_element(By.XPATH, '//*[@id="u-1238065328"]/main/div[1]/div/div[3]/button[2]')
reject_to_see_likes.click()
time.sleep(2)

like_button = driver.find_element(By.XPATH, '//*[@id="u490315748"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button')
disallow_notifications.click()
time.sleep(3)



# the X button  //*[@id="u490315748"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[2]/button