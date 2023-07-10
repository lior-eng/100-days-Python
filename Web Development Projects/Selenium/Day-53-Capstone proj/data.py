from bs4 import BeautifulSoup
import requests

class Data:
    
    def __init__(self, url: str) -> None:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9"
        }
        response = requests.get(url, headers= headers)
        zillow_web_page = response.content
        self.soup = BeautifulSoup(zillow_web_page, "html.parser")

    def get_links(self) -> list[str]:
        links = self.soup.find_all(name= "a", class_= "gZUDVm")
        apartment_links: list[str] = []
        for link in links:
            apartment_links.append(link.get("href"))
        return apartment_links
    
    def get_address(self) -> list[str]:
        addresses = self.soup.find_all(name= "address")
        apartment_addresses: list[str] = []
        for address in addresses:
            apartment_addresses.append(address.get_text())
        return apartment_addresses
    
    def get_prices(self) -> list[int]:
        preices = self.soup.find_all(name= "span", class_= "iMKTKr")
        apartment_prices: list[int] = []
        for price in preices:
            number = price.get_text().split("$")[1]
            if "+" in number:
                number = number.split("+")[0]
            elif "/" in number:
                number = number.split("/")[0]
            apartment_prices.append(number)
        return apartment_prices