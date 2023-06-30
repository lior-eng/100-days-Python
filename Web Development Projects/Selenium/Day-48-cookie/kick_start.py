from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_drive_path = "C:/Users/user/Desktop/chromedriver.exe"
service = Service(executable_path=chrome_drive_path)

options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
driver = webdriver.Chrome(options=options, service=service)

# driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")

# price_element = driver.find_element(By.CLASS_NAME, "a-offscreen")
# print(price_element.get_attribute("textContent"))

# driver.get("https://www.python.org")

# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.tag_name)

# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

##### challenge Upcoming Events ###########

driver.get("https://www.python.org")

events_dates:list = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names:list = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
upcoming_events: dict = {}

for index in range (len(event_names)):
    upcoming_events[index] = {
        "date": events_dates[index].text,
        "name": event_names[index].text
    }
    
print(upcoming_events)

# driver.quit()