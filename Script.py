import os
from twilio.rest import Client as cs
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse as mr
import json
# import creds
from threading import Thread
import test
from textblob import TextBlob


app = Flask(__name__)

account_sid = os.environ['account_sid']
auth_token = os.environ['auth_token']
client = cs(account_sid, auth_token)

app = Flask(__name__)
# account_sid = creds.account_sid
# auth_token = creds.auth_token

# client = cs(account_sid, auth_token)

# client.messages.create(
#     to = creds.phone_number,
#     from_ = "+19032518533",
#     body= "hello world!"
# )

k = ""

@app.route('/', methods=['POST', 'GET'])
def sms_reply():
    global k
    response = mr()
    body = request.values.get('Body', None)
    if body == "I'm tired":
        k = body
        print(k)
        res = TextBlob(k)
        print(res.sentiment.polarity)
    response.message("jjj")
    return str(response)

def run():
    app.run(host='0.0.0.0',port=9090)

def keep_alive():
    t = Thread(target=run)
    t.start()
    
keep_alive()