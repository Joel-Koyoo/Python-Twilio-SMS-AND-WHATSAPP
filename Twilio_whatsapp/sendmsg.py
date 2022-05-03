from twilio.rest import Client
sid='AC092e85c3b9606a568439ada193f4afd8'
authToken='73872bc1cfb021d6e4e18bf95a401c11'
client =Client(sid,authToken)
message=client.messages.create(
        to='whatsapp:+254727243892',
        from_='whatsapp:+14155238886',
        body='Hello welcome to urban Farmer. Your one stop shop for all your agricultural need. \n Kindly reply with a number to know more about a crop\n 1. Maize \n 2. Beans \n 3. Wheat \n 4. Banana \n 5.Sugarcane')