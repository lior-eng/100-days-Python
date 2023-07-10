from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class Bot:
    
    def __init__(self, chrome_driver_path: str) -> None:
        service = Service(executable_path= chrome_driver_path)
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.driver = webdriver.Chrome(options= options, service= service)
        
    def fill_format(self, url: str, address: str, price: int, link: str) -> None:
        self.driver.get(url)
        time.sleep(3)
        
        first_question = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        first_question.send_keys(address)
        time.sleep(1)
        
        second_question = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        second_question.send_keys(f"{price}")
        time.sleep(1)
        
        third_question = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        third_question.send_keys(link)
        time.sleep(1)
        
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
        submit_button.click()
        time.sleep(2)
        
    def submit_another_response(self) -> None:
        button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        button.click()
        time.sleep(2)
        