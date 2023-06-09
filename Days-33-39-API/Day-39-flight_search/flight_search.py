import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = "wy7T6Ko0RGTnKLnEeitJLZlANOsDYsFr"

class FlightSearch:
    
    def __init__(self) -> None:
        pass
    
    def get_destination_code(self, city_name: str) -> str:
        locations_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url= locations_endpoint,
                            headers= headers,
                            params= query)
        result = response.json()["locations"]
        code = result[0]["code"]
        return code
    
    def search_flights(self,
                       origin_city_code: str,
                       tomorrow: str,
                       six_months_from_today: str,
                       destination_airport_code: str) -> FlightData:
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_airport_code,
            "date_from": tomorrow,
            "date_to": six_months_from_today,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "curr": "GBP",
            "max_stopovers": 0
        }
        response = requests.get(url= f"{TEQUILA_ENDPOINT}/v2/search",
                     headers= headers,
                     params= query)
        data = response.json()["data"][0]
        
        '''
        In the under fligh data object the
        "route" is the relevant data about the flight
        '''
        flight_data = FlightData(
            price = data["price"],
            origin_city = data["route"][0]["cityFrom"], 
            origin_airport = data["route"][0]["flyFrom"],
            destination_city = data["route"][0]["cityTo"],
            destination_airport = data["route"][0]["flyTo"],
            flight_date = data["route"][0]["local_departure"].split("T")[0],
            return_date = data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: {flight_data.price}")
        return flight_data