import re
import config
import smtplib
import requests
from pprint import pprint
from bs4 import BeautifulSoup

MY_URL = "https://www.amazon.co.uk/gp/product/B00K5ZKA0U/ref=ox_sc_act_title_1?smid=A3P5ROKL5A1OLE&psc=1"
my_headers = {
    'Accept-Language': 'en-GB;en-US',
    'User-Agent': 'Chrome/113.0.0.0'
}

response = requests.get(url=MY_URL, headers=my_headers)

soup = BeautifulSoup(response.content, "lxml")

item_name_data = soup.find(name="span", id="productTitle")
split_delimiter = "-"
item_name_string = item_name_data.getText()

item_name = re.split(split_delimiter, item_name_string)[0].strip()

item_price_data = soup.find(name="span", class_="a-price")
item_price_string = item_price_data.select_one(
    "span.a-offscreen").getText()[1:]
item_price = float(item_price_string)


# Email notification code
if item_price <= 10:
    SMTP_SERV = config.SMTP_SERV
    SENDER_EMAIL = config.sender_email
    SENDER_PASS = config.sender_pass
    DEST_EMAIL = config.dest_email
    MSG = f"Subject: PRICE ALERT FOR AMAZON ITEM!\n\nOnly £{item_price} for your Amazon tracked {item_name}.".encode(
        "utf-8")

    with smtplib.SMTP(config.SMTP_SERV) as email_connection:
        email_connection.starttls()
        email_connection.login(user=SENDER_EMAIL, password=SENDER_PASS)
        email_connection.sendmail(from_addr=SENDER_EMAIL,
                                  to_addrs=DEST_EMAIL,
                                  msg=MSG)
        print("Email sent successfuly.")
