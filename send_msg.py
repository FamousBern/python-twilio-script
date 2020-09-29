# Twilio api trial account.

# Packages required
# https://schedule.readthedocs.io/en/stable/
# pip install schedule

# https://www.twilio.com/docs/libraries/python
# pip install twilio

# or run python pip install requirements.txt to install all the packages

from twilio.rest import Client

import random
import schedule
import time

# quotes = ['Good morning! This is from Bernard, wishing you a happy day.', 'Hello there!']

# quote = random.choice(quotes)


# Function definition to send our message
def send_message():
    account_sid = ''
    auth_token = ''

    cellphone = ''
    twilio_num = ''

    quote = 'Good morning Liz. I hope you had a great night sleep.'

    client = Client(account_sid, auth_token)

    msg = client.messages.create(to = cellphone, from_ = twilio_num, body = quote)
    return msg

schedule.every().day.at("09:49").do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)