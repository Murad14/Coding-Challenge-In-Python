import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "*********@gmail.com"
MY_PASSWORD = "***********" #App password
now = dt.datetime.now()
today = (now.month, now.day)

data_sheet = pandas.read_csv('birthdays.csv')

birthdays_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in data_sheet.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_select =f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_select) as f:
        contents = f.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{contents}")