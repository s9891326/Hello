import os
from twilio.rest import Client


# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
account_sid = 'AC8ac01724e18b8f7e968696bf1e33c2f0'
auth_token = 'c78f3faca003b2c482b0ff740a0fc4c4'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/classic.mp3',
                        twiml='<Response><Say>Hello, World!</Say></Response>',
                        to='+886929100148',
                        # to='+886972858150',
                        from_='+19124234899'
                    )

print(call.sid)

# message = client.messages \
#     .create(
#          body='This is the ship that made the Kessel Run in fourteen parsecs?',
#          from_='++19124234899',
#          to='+886929100148'
#      )
#
# print(message.sid)
