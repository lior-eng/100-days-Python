import smtplib
import datetime as dt
import pandas as pd
import random

# MY_EMAIL =
# MY_PASSWORD = 
PLACE_HOLDER = "[NAME]"

data: pd.DataFrame = pd.read_csv("./Day-32 SMTP/birthdays.csv")
now = dt.datetime.now()
day_in_month: int = now.day
month: int = now.month

for index, _ in data.iterrows():
    if day_in_month == int(data["day"][index]) and month == int(data["month"][index]):
        letter_number = random.randint(1, 3)
        with open(f'./Day-32 SMTP/letter_{letter_number}.txt', mode= 'r') as letter_file:
            letter_content: str = letter_file.read()
            sent_to = data["name"][index]
            letter_with_name = letter_content.replace(PLACE_HOLDER, sent_to)
            print(letter_with_name)
    
        # with smtplib.SMTP("smtp.gmail.com") as connection:
            # connection.starttls()
            # connection.login(user= MY_EMAIL, password= MY_PASSWORD)
            # connection.sendmail(from_addr= MY_EMAIL,
                            # to_addrs= some mail,
                            # msg= F"Subject:from vs code\n\n{letter_with_name}") 