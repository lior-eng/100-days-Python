import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(URL, headers= headers)
amazon_web_page = response.content

soup = BeautifulSoup(amazon_web_page, "lxml")
price = soup.find(class_= "a-offscreen").get_text()
product_title = soup.select_one("h1 span").get_text().strip()
price:float = price.split("$")[1]