from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH = "C:/Users/user/Desktop/chromedriver.exe"

class InternetSpeedTwitterBot:
    
    def __init__(self, chrome_driver_path: str) -> None:
        service = Service(executable_path= chrome_driver_path)
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.driver = webdriver.Chrome(options= options, service= service)
        self.up = 0
        self.down = 0
        
        
    def get_internet_speed(self) -> None:
        self.driver.get("https://www.speedtest.net/")
        time.sleep(12)
        cookie_button = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        cookie_button.click()
        time.sleep(2)
        
        go_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        go_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()
        time.sleep(60)
        
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(self.down.text, self.up.text)
        
    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        time.sleep(5)
        
        user_name = self.driver.find_element(By.NAME, "text")
        user_name.send_keys("")
        time.sleep(2)

        next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
        next_button.click()
        time.sleep(3)
        
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("")
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        
        tweet = "Hi you"
        time.sleep(1)
        
        status_tab = self.driver.find_element(By.XPATH, '//div[@aria-label="Tweet text"]')
        status_tab.send_keys(tweet)
        time.sleep(2)
       
        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]')
        tweet_button.click()
        time.sleep(2)

# obj = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
# obj.tweet_at_provider()