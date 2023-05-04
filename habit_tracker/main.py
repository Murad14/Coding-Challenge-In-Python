import requests
from datetime import datetime

USERNAME = "murad21"
TOKEN ="fdsjkqj12nuoh**********"
GRAPH = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_param = {
    "token" : TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

# response = requests.post(url=pixela_endpoint, json=user_param)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Tracking Graph for Coding",
    "unit": "commit",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json= graph_config, headers= headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"

today = datetime.now()
# print(today.strftime("%d,%B,%Y"))

pixel_data = {
    "date": today.strftime("%Y%m%d"), #dateformetbyYYYYmmDD
    "quantity": input("Input today's total commit: "),
}

response = requests.post(url=pixel_creation_endpoint, json= pixel_data, headers= headers)
print(response.text)

update_end_point = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "15"
}

# response = requests.put(url=update_end_point, json= new_pixel_data, headers=headers)
# print(response.text)

delete_end_point = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_end_point, headers=headers)
# print(response.text)