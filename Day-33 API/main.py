import requests
from datetime import datetime
import smtplib

# MY_EMAIL = 
# MY_PASSWORD = 

MY_LAT = 32.085300
MY_LONG = 34.781769

def is_iss_overhead() -> bool:
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_lat = float(iss_data["iss_position"]["latitude"])
    iss_lng = float(iss_data["iss_position"]["longitude"])
    
    if MY_LONG - 5 <= iss_lng <= MY_LONG + 5 \
        and MY_LAT - 5 <= iss_lat <= MY_LAT + 5:
        return True
    return False

def is_night() -> bool: 
    parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
    }     
    response = requests.get(url= 'https://api.sunrise-sunset.org/json',
                            params= parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    
    if sunset <= time_now or time_now <= sunrise:
        return True
    return False

# if is_iss_overhead() and is_night():
#     print("here")
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user= MY_EMAIL, password= MY_PASSWORD)
#         connection.sendmail(from_addr= MY_EMAIL,
#                         to_addrs= some Email,
#                         msg= F"Subject:from vs code\n\n ISS is here") 