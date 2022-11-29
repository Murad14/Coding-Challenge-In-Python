import requests
from twilio.rest import Client
import os


OWM_Endpoint = "http://api.weatherapi.com/v1/current.json?key=API_KEY=Chittagong&aqi=no"
account_sid ="ACef0f4ca0f9338e3ef000218a0e1ee344"
auth_token = os.environ.get("AUTH_TOKEN")


response =requests.get(OWM_Endpoint)
response.raise_for_status()
weather_data = response.json()
weather_status = weather_data["current"]["condition"]["text"]
weather_code = weather_data["current"]["condition"]["code"]
if weather_code == 1006:
    client = Client(account_sid,auth_token)
    message = client.messages \
        .create(
        body="Sky will be cloudy today. Remember to bring an ☂️",
        from_='+18176704300',
        to='+880********'
    )

    print(message.status)