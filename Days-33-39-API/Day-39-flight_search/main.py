from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

ORIGIN_CITY_CODE = "TLV"

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
print(sheet_data)

flight_search = FlightSearch()
notification_manager = NotificationManager()

if sheet_data[0]["iataCode"] == "":
    for row_data in sheet_data:
        row_data["iataCode"] = flight_search.get_destination_code(row_data["city"])
    
    data_manager.get_destination_data = sheet_data
    data_manager.update_destination_codes()

today = datetime.now()
tomorrow = (today + timedelta(days= 1)).strftime("%d/%m/%Y")
six_months_from_today = (today + timedelta(days= 6*30)).strftime("%d/%m/%Y")

for destination in sheet_data:
    flight = flight_search.search_flights(ORIGIN_CITY_CODE,
                                    tomorrow,
                                    six_months_from_today,
                                    destination["iataCode"])
    if flight.price < destination["lowestPrice"]:
        message_body = f"Low price alert! Only {flight.price} GBP from" \
                    f"{flight.origin_city}-{flight.origin_airport} to " \
                    f"{flight.destination_city}-{flight.destination_airport}, " \
                    f"from date {flight.flight_date} to {flight.return_date}."
        notification_manager.send_sms(message_body)


    
    