import requests
from pprint import pprint

# SHEETY_ENDPOINT = "https://api.sheety.co/ffcc6a482cd422850d1325986f9d41b3/flightDeals/prices" # my
SHEETY_ENDPOINT = "https://api.sheety.co/86a81c7aba9393c4d6833e6f387d1225/flightDeals/prices" # gal

class DataManager:
            
    def __init__(self) -> None:
        self.destination_data = {}
    
    def get_destination_data(self) -> list[dict]:
        data = requests.get(url= SHEETY_ENDPOINT)
        self.destination_data = data.json()["prices"]
        return self.destination_data
    
    def update_destination_codes(self) -> None:
        for city in self.destination_data:
            update_data: dict[str, str] = {
                "price": {
                    "iataCode": city["iataCode"],
                }
            }
            response = requests.put(url= f"{SHEETY_ENDPOINT}/{city['id']}",
                                    json= update_data)
        print(response.text)
        