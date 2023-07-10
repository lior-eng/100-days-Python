from data import Data
from bot import Bot

CHROME_DRIVER_PATH = "C:/Users/user/Desktop/chromedriver.exe"
ZILLOW_URL = "https://tinyurl.com/5djr27fu"
FORM_URL = "https://forms.gle/vGdeWgzLDT6K9XAn9"
RESPONSES_URL = "https://docs.google.com/forms/d/1H9VK7Hxltys84AX8IaCHpRzdbtHrEzUPIN9PPHxw7Pc/edit#responses"

data = Data(ZILLOW_URL)
addresses = data.get_address()
links = data.get_links()
prices = data.get_prices()

bot = Bot(CHROME_DRIVER_PATH)
bot.fill_format(RESPONSES_URL)

number_of_apartment = len(addresses)
for index in range (number_of_apartment):
    bot.fill_format(FORM_URL, addresses[index], prices[index], links[index])
    bot.submit_another_response()