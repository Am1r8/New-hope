from email.quoprimime import quote
import os
from twilio.rest import Client as cs
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse as mr
import json
# import creds
from threading import Thread
import test
from textblob import TextBlob
import random

app = Flask(__name__)

user_Request = ""
account_sid = os.environ['account_sid']
auth_token = os.environ['auth_token']
client = cs(account_sid, auth_token)


response_sad = ["I'm so sorry that everything sucks so much right now. I love you, everyone loves you :).", "Did you drink water and eat today? I can Postmates you something yummy.", "Remember to do something kind for yourself today! Take a bath, drink some wine, and watch a bad movie.", "I admire how creative you are. You've always had such an eye for style. You don't have to worry about anything :)", "It's OK to cry and be upset. Don't feel any pressure to be #goodvibesonly.", "we all feel sad sometimes, there is nothing we can do about it. it's in human nature. don't forget that I love you and you matter to me :)"]
response_happy = ["Your message made me do this 😄.", "Every notification from you just makes me light up.", "I want to print out that message and frame it. Honestly, it’s so beautiful. Thank you!", "Aw I’m speechless. Your message made me 🥺.", "Nothing I could text back would be as amazing as your message.", "that's great to hear, I'm happy that you are happy"]
response_neutral = ["I'm sorry I did not catch that can you repeat please :)", "I'm sorry, I didn't understand that. Please try again.", "sorry my computer brain didn't hear that can you repeat", "awwwwww, sorry I didn't catch that can you repeat"]
joke = ["What’s the best thing about Switzerland???? I don’t know, but the flag is a big plus.", "Did you hear about the mathematician who’s afraid of negative numbers???? He’ll stop at nothing to avoid them.", "A ham sandwich walks into a bar and orders a beer, bartender says “sorry, we don’t serve food here.”", "Why did the Clydesdale give the pony a glass of water? Because he was a little horse.", "What do you call a fish without eyes? Fsh.", "What do you call an alligator detective? An investi-gator.", "Why did the scarecrow win an award? Because he was outstanding in his field.", "What lights up a soccer stadium? A soccer match."]
quotes = ["The purpose of our lives is to be happy.", "Life is what happens when you’re busy making other plans.", "Get busy living or get busy dying.", "You only live once, but if you do it right, once is enough.", "Many of life’s failures are people who did not realize how close they were to success when they gave up.", "If you want to live a happy life, tie it to a goal, not to people or things.", "Never let the fear of striking out keep you from playing the game.", "Money and success don’t change people; they merely amplify what is already there.", "Your time is limited, so don’t waste it living someone else’s life. Don’t be trapped by dogma – which is living with the results of other people’s thinking.", "Not how long, but how well you have lived is the main thing."]
advice = ["Stay true to yourself.", "Do what you love--not what you're told to love.", "Create the environment that's right for you.", "Choose your friends wisely.", "Develop positive habits.", "Create certainty and leave room for uncertainty.", "Be vulnerable.", "Don't make assumptions.", "Be patient and persistent", "Luck comes from hard work.", "Life's good, but it's not fair."]
activity = ["Organize your basement.", "Learn how to make a website", "Go for a run", "Create a meal plan", "make a new music playlist", "listen to a new music genre", "Go swimming with a friend or alone", "paint the first thing you see in your room", "update your resume", "make a paper plane", "meditate"]
nums = ["8", "10"]

# account_sid = creds.account_sid
# auth_token = creds.auth_token

# client = cs(account_sid, auth_token)

# client.messages.create(
#     to = creds.phone_number,
#     from_ = "+19032518533",
#     body= "hello world!"
# )



@app.route('/', methods=['POST', 'GET'])
def sms_reply():
    global user_Request
    response = mr()
    body = request.values.get('Body', None)
    user_Request = (str(body))
    if user_Request != "":
        res = TextBlob(user_Request)
        polarity = res.sentiment.polarity
        print(polarity)
    if user_Request == "How does this work?":
        response.message("We all feel sad or happy sometimes, there is nothing we can do about it. it's in human nature. New hope is here to help people, we want to show people that they matter, we want to show how people love eachother! Mental health is an important thing and we have to pay more attention to it.\nmy commands:\n'0' HELP\n'1' I really need help\n'2' SUICIDE HOTLINE\n'3' JOKE\n'4' QUOTE\n'5' I'm bored\n'6' LIFE ADVICE\n'7' ABOUT DEV\nOr if you want you can just talk to me! I'm always here for you ❤️️")
        return str(response)
    if user_Request == "0":
        response.message("You requested: HELP")
        response.message("How can I help?!\nJust talk to me I'm here to listen to you only ❤️️")
        return str(response)
    elif user_Request == "1":
        response.message("You requested: I really need help")
        response.message("I can give you phone numbers of therapist, we all need to talk to someone.")
        response.message("You can visit https://www.goodtherapy.org/find-therapist.html to find a good therapist!")
        return str(response)
    elif user_Request == "2":
        response.message("You requested: SUICIDE HOTLINE")
        response.message("Call 833-456-4566")
        response.message("You can visit https://findahelpline.com/ to find help too")
        return str(response)
    elif user_Request == "3":
        response.message("You requested: JOKE")
        response.message(random.choice(joke))
        return str(response)
    elif user_Request == "4":
        response.message("You requested: QUOTES")
        response.message(random.choice(quotes))
        return str(response)
    elif user_Request == "5":
        response.message("You requested: I'm bored")
        response.message(random.choice(activity))
        return str(response)
    elif user_Request == "7":
        response.message("You requested: ABOUT DEV")
        response.message("I'm a bot made by Amirhosein Soleimanian. I was created to help people feel better. I'm not perfect, but I'm trying. If you have any questions or concerns, please contact me at instgram @am1r__8")
        return str(response)
    elif user_Request == "6":
        response.message("You requested: Life Advice")
        response.message(random.choice(advice))
        return str(response)
    elif user_Request == "9":
        response.message("You requested: Commands")
        response.message("my commands:\nmy commands:\n'0' HELP\n'1' I really need help\n'2' SUICIDE HOTLINE\n'3' JOKE\n'4' QUOTE\n'5' I'm bored\n'6' LIFE ADVICE\n'7' ABOUT DEV\nOr if you want you can just talk to me! I'm always here for you ❤️️")
        return str(response)
    elif user_Request in nums:
        response.message(random.choice(response_neutral))
        return str(response)
    if polarity < 0.5 or polarity > 0:
        response.message(random.choice(response_sad))
    elif polarity == 0:
        response.message(random.choice(response_neutral))
    elif polarity > 0:
        response.message(random.choice(response_happy))
    elif polarity < 0:
        response.message(random.choice(response_sad))
    return str(response)

def run():
    app.run(host='0.0.0.0',port=9090)

def keep_alive():
    t = Thread(target=run)
    t.start()
    
keep_alive()