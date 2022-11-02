import os
from twilio.rest import Client


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
# account_sid = 'AC8ac01724e18b8f7e968696bf1e33c2f0'
# auth_token = '2e1b38236a5c45144903442d33b8366a'
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='MG0067298bd6d6510cce0512f4e6bffdd5',
    body='hello world!',
    to='+886939552676'
)

print(message.sid)

# call = client.calls.create(
#                         url='http://demo.twilio.com/docs/classic.mp3',
#                         twiml='<Response><Say>Hello, World!</Say></Response>',
#                         to='+886929100148',
#                         # to='+886972858150',
#                         from_='+19124234899'
#                     )
#
# print(call.sid)

# message = client.messages \
#     .create(
#          body='This is the ship that made the Kessel Run in fourteen parsecs?',
#          from_='++19124234899',
#          to='+886929100148'
#      )
#
# print(message.sid)
