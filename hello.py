# Step 1: [Text Messages] Have A Collection of Preset Messages We Can Send my_messages = [" ", " "]""

GOOD_MORNING_QUOTES = [
    "Good Morning Sunshine ☀️"
    "Good Morning Beautiful"
    "You're my number 1 reason I look forward to waking up"
]

# Step 2: [Send To Our LOML] Send Preset Message Using API send_message(my_messages[0])

# 1. import thr twilio client
from twilio.rest import Client
import schedule
import random

cellphone = 5615370225
twilio_number = 8305810766

# 2. created a function that can take in and send a message
def send_message(quote):
    account = ""
    token = ""
    client = Client(account,token)

    # Call the function
    client.messages.create(
    to=cellphone,
    from_=twilio_number,
    body=quote)

    # Use Library that can schedule the message every morning to the LOML at a certain time
    quote = GOOD_MORNING_QUOTES[random.randint(0, len(GOOD_MORNING_QUOTES))]
    schedule.every().day.at("07:00").do(send_message, GOOD_MORNING_QUOTES[0])