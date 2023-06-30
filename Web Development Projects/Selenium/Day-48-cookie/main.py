from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "C:/Users/user/Desktop/chromedriver.exe"
service = Service(executable_path= chrome_driver_path)

options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
driver = webdriver.Chrome(options= options, service= service)

driver.get("https://orteil.dashnet.org/experiments/cookie/")


########## First Bot ##########

# cookie = driver.find_element(By.ID, "cookie")

# items = driver.find_elements(By.CSS_SELECTOR, "#store div")
# items_ids = [item.get_attribute("id") for item in items]

# check_available_products = time.time() + 5
# timer = time.time() + 60 * 5

# while True:
#     cookie.click()

#     if time.time() > check_available_products:
        
#         all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
#         item_prices:list = []
        
#         for price in all_prices:
#             item_text = price.text
#             if item_text != "":
#                 item_price = int(item_text.split("-")[1].strip().replace(",", ""))
#                 item_prices.append(item_price)
        
#         upgrades_prices: dict = {}
#         for index in range(len(item_prices)):
#             upgrades_prices[items_ids[index]] = item_prices[index]
        
#         cookies_amount = driver.find_element(By.ID, "money").text
#         if "," in cookies_amount:
#             cookies_amount = int(cookies_amount.replace(",", ""))
            
#         available_upgrades:dict = {}
#         for id, price in upgrades_prices.items():
#             if price < int(cookies_amount):
#                 available_upgrades[id] = price
                
#         highest_item_available = max(available_upgrades)
#         if highest_item_available != "buyCursor":
#             to_buy = driver.find_element(By.ID, highest_item_available).click()
#             print(highest_item_available)
    
#         check_available_products = time.time() + 5
        
#     if timer < time.time():
#         cookies_per_sec = driver.find_element(By.ID, "cps").text
#         print(cookies_per_sec)
#         break

########## Second Bot ##########

cookie = driver.find_element(By.ID, "cookie")
cookies_amount = driver.find_element(By.ID, "money").text

timer = time.time() + 60 * 5
 
while True:
    check_available_products = time.time() + 5

    while time.time() < check_available_products:
        cookie.click()   
    cookies_amount = driver.find_element(By.ID, "money").text.replace(",", "")

    shipment = driver.find_element(By.XPATH, "//*[@id='buyShipment']/b")
    shipment_price = shipment.text.split("-")[1].strip().replace(",", "")
    
    mine = driver.find_element(By.XPATH, "//*[@id='buyMine']/b")
    mine_price = mine.text.split("-")[1].strip().replace(",", "")

    factory = driver.find_element(By.XPATH, "//*[@id='buyFactory']/b")
    factory_price = factory.text.split("-")[1].strip().replace(",", "")
    
    grandma = driver.find_element(By.XPATH, "//*[@id='buyGrandma']/b")
    grandma_price = grandma.text.split("-")[1].strip().replace(",", "")

    cursor = driver.find_element(By.XPATH, "//*[@id='buyCursor']/b")
    cursor_price = cursor.text.split("-")[1].strip().replace(",", "")
    
    if int(shipment_price) <= int(cookies_amount):
        time.sleep(0.1)
        shipment.click()
    
    elif int(mine_price) <= int(cookies_amount) and int(mine_price) <= int(shipment_price) // 2:
        time.sleep(0.1)
        mine.click()
        
    elif int(factory_price) <= int(cookies_amount) and int(factory_price) <= int(mine_price) // 2:
        time.sleep(0.1)
        factory.click()

    elif int(grandma_price) <= int(cookies_amount) and int(grandma_price) <= int(factory_price) // 4:
        time.sleep(0.1)
        grandma.click()
        
    elif int(cursor_price) <= int(cookies_amount) and int(cursor_price) <= int(grandma_price) // 8:
        time.sleep(0.1)
        cursor.click()
    if timer  < time.time():
        cookies_per_sec = driver.find_element(By.ID, "cps").text
        print(cookies_per_sec)
        break
