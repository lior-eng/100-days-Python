
class FlightData:
    
    def __init__(self,
                 price:int,
                 origin_city: str,
                 origin_airport: str,
                 destination_city: str,
                 destination_airport: str,
                 flight_date: str,
                 return_date: str) -> None:
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.flight_date = flight_date
        self.return_date = return_date
        
    # def check_price(self, sheet_price: int) -> bool:
    #     if sheet_price < self.price:
    #         return True
    #     else:
    #         return False