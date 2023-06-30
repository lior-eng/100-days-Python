import requests
import os
from datetime import datetime

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ['API_KEY']

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ['sheet_endpoint']

exercise_text = input("Tell me which exercises you did: ")

exercise_params = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 79.5,
    "height_cm": 180.0,
    "age": 32
}

exercise_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

exercise_response = requests.post(url= exercise_endpoint,
                                  json= exercise_params,
                                  headers= exercise_headers)
result = exercise_response.json()

today = datetime.now()
today_date = today.strftime("%d/%m/%Y")
now_time = today.strftime("%X")

Authorization_token = os.environ['Authorization_token']

bearer_headers = {
    "Authorization": f"Bearer {Authorization_token}"
}

response = requests.get(sheet_endpoint, headers= bearer_headers)

for exercise in result["exercises"]:
    row_data = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

add_row_response = requests.post(url= sheet_endpoint,
                                 json= row_data,
                                 headers= bearer_headers)
print(add_row_response.text)