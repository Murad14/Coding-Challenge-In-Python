import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "39Q7Y7UBF******"
NEWS_API_KEY = "2cc6f1dec*****e3bf"
TWILIO_SID = "ACef0f4ca************18a0e1ee344"
TWILIO_AUTH_TOKEN = "ec370235b*********f36b1d877"

stock_params = {
    "function": "TIME_SERIES_WEEKLY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT,params=stock_params)
data = response.json()["Weekly Time Series"]
data_list = [value for (key, value) in data.items()]
weekly_data = data_list[0]
weekly_data_closing_price = weekly_data["4. close"]
print(weekly_data_closing_price)

week_before_week_data = data_list[1]
week_before_week_closing_data = week_before_week_data["4. close"]
print(week_before_week_closing_data)

difference = float(weekly_data_closing_price) - float(week_before_week_closing_data)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference / float(weekly_data_closing_price)) * 100)
print(diff_percent)

if abs(diff_percent) > 8:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3] #slicing
    print(three_articles)

formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}% \nHeadline: {article['title']}. \nBrief: " \
                      f"{article['description']}" for article in three_articles]

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
for article in formatted_articles:
    message = client.messages.create(
                body=article,
                from_='+18176704300',
                to='+880**********'
            )
    print(message.sid)

