import os
from twilio.rest import Client
from dotenv import load_dotenv


load_dotenv()

account_sid=os.getenv('TWILIO_ACCOUNT_SID')
auth_token=os.getenv('TWILIO_AUTH_TOKEN')

client=Client(account_sid,auth_token)

message = client.messages \
    .create(
        body="Hello welcome to urban Farmer. Your one stop shop for all your agricultural need. \n Kindly reply with a number to know more about a crop\n 1. Maize \n 2. Beans \n 3. Wheat \n 4. Banana \n 5.Sugarcane'",
        from_='+16065546438',
        media_url=['https://plantvillage-production-new.s3.amazonaws.com/images/pics/000/004/892/original/8266592682_fc84edb59d_z.jpg'],
        to='+254727243892'
    )
    
print(message.sid)
    