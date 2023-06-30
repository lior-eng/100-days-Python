from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_drive_path = "C:/Users/user/Desktop/chromedriver.exe"
service = Service(executable_path=chrome_drive_path)

options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
driver = webdriver.Chrome(options=options, service=service)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_counts = driver.find_element(By.CSS_SELECTOR, "[title= 'Special:Statistics']")
# article_counts = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(article_counts.text)
# article_counts.click()

# press_on_link = driver.find_element(By.LINK_TEXT, "free")
# press_on_link.click()

# search = driver.find_element(By.NAME, "search")
# search.click()
# search.clear()

##### challenge #####

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Python")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Snake")

mail_address = driver.find_element(By.NAME, "email")
mail_address.send_keys("sdfsdfj@sds.com")

button = driver.find_element(By.CSS_SELECTOR, ".btn-block")
button.click()
time.sleep(3)