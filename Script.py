import os
from twilio.rest import Client as cs
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse as mr
import creds

account_sid = creds.account_sid
auth_token = creds.auth_token

client = cs(account_sid, auth_token)

# client.messages.create(
#     to = creds.phone_number,
#     from_ = "+19032518533",
#     body= "hello world!"
# )

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def sms_reply():
    resp = mr()
    resp.message("Hello! You said: ")
    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)