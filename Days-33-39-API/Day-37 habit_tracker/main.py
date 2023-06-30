import requests 
from datetime import datetime

USER_NAME = "Something"
TOKEN = "Something"
GRAPH_ID = "Something"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url= pixela_endpoint, json= user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# graph_response = requests.post(url= graph_endpoint, json= graph_config, headers= headers)
# print(graph_response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

today: str = datetime.now().strftime("%Y%m%d")

pixel_params: dict[str, str] = {
    "date": today,
    "quantity": "8.4"
}

# pixel_creation_response = requests.post(url= pixel_creation_endpoint, json= pixel_params, headers= headers)
# print(graph_response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today}"

update_params: dict[str, str] = {
    "quantity": "3.4",
}

# update_pixel_response = requests.put(url= update_pixel_endpoint, json= update_params, headers= headers)
# print(update_pixel_response.text)

delete_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today}"

delete_pixel_response = requests.delete(url= delete_pixel_endpoint, headers= headers)
print(delete_pixel_response.text)
