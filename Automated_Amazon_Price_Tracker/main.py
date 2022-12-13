import requests
from bs4 import BeautifulSoup
import smtplib

MY_EMAIL = "muradulalam4@gmail.com"
MY_PASSWORD = "################" #removed for security purpose
BUY_PRICE = 200
SMTP_ADDRESS = "muradul_alam@yahoo.com"

URL = "https://www.amazon.com/NuWave-Nutri-Pot-Stainless-Sure-Lock-Technology/dp/B09F6XHB4C/?_encoding=UTF8&pd_rd_w=4" \
      "btKI&content-id=amzn1.sym.920be9b9-7b18-41cf-ace1-88f9dfc0e2c4&pf_rd_p=920be9b9-7b18-41cf-ace1-88f9dfc0e2c4&pf_rd" \
      "_r=WFEABAB45GY8GJRH6B3R&pd_rd_wg=EY6QY&pd_rd_r=02419177-cb4c-46e5-bbec-d2f50c82d185&ref_=pd_gw_deals_ct&th=1"

HEADERS = {
    'Accept-Language' : "en-GB,en-US;q=0.9,en;q=0.8,bn;q=0.7",
    'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 "
                   "Safari/537.36",
    'Accept-Encoding' : "gzip, deflate",
    'Cookie' : "_ga=GA1.2.107394614.1670874542; _gid=GA1.2.1482566027.1670874542",
    'Connection' : "keep-alive"
    }

response = requests.get(URL, headers=HEADERS)
data = response.text
soup = BeautifulSoup(data, "lxml")
# print(soup.prettify())

price = soup.find(name="span", class_= "a-price-whole").get_text()
product_price = float(price.replace("$", "").replace(",", ""))
# print(product_price)
title = soup.find(id= "productTitle").get_text().strip()
# print(title)


if product_price < BUY_PRICE:
    message = f"{title} is now ${product_price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=SMTP_ADDRESS,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
        )
