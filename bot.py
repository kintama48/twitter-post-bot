import json
import os
import platform
import sys

import discord
import psycopg2
import requests
import tweepy
from discord.ext.commands import Bot

if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)

API_KEY = config["API_key"]
API_SECRET = config["API_secret"]
ACCESS_KEY = config["access_key"]
ACCESS_SECRET = config["access_secret"]
USER_TO_SNITCH = config["user_handle"]
DISCORD_BOT_TOKEN = config["token"]
REQUEST_CHANNEL_ID = config["requests_channel_id"]

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)
user = api.get_user(screen_name=USER_TO_SNITCH)

# auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
# url = auth.get_authorization_url()
# print(url)
# verifier = input("Enter code: ")
# access = auth.get_access_token(verifier)
# print(access)

bot = Bot(command_prefix=config["bot_prefix"], intents=discord.Intents.default())

# ('1117644298441379843-EyfBPZ52PJs7WoMt54yXbJnHpAIPA6', 'tXNp5hViTOxPiZ2HL92Z583UZDSJKA8kfqslqW4kuqGC0')


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    print(f"Discord.py API version: {discord.__version__}")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    # db = psycopg2.connect(database="iwbvxkaz", user="iwbvxkaz", password="HV07JILUzmh7xNaxKg1t_29NxoLci6Uc",
    #                       host="rosie.db.elephantsql.com", )
    # cur = db.cursor()
    # cur.execute("UPDATE public.count SET num=0;")
    # db.commit()
    # cur.close()
    # db.close()


@bot.event
async def on_message(message):
    if message.channel.id == REQUEST_CHANNEL_ID:
        if int(message.author.id) == 442264225428275201:
            db = psycopg2.connect(database="iwbvxkaz", user="iwbvxkaz", password="HV07JILUzmh7xNaxKg1t_29NxoLci6Uc",
                                  host="rosie.db.elephantsql.com")
            cur = db.cursor()
            cur.execute("SELECT num FROM public.count;")
            temp = cur.fetchone()[0] + 1

            if not temp % 3:
                if len(message.attachments) > 0:
                    print(message.attachments[0])
                    tweet_media(message.content, message.attachments[0])
                    cur.execute("UPDATE public.count SET num=0;")
                    db.commit()
                    cur.close()
                    db.close()
                else:
                    returned = tweet_media(message.content)
                    if returned:
                        message.channel.send(returned)
                    cur.execute("UPDATE public.count SET num=0;")
                    db.commit()
                    cur.close()
                    db.close()

            else:
                cur.execute(f"UPDATE public.count SET num = ({temp});")
                db.commit()
                cur.close()
                db.close()


def tweet_media(message, link=None):
    if link:
        request = requests.get(link, stream=True)
        filename = "temp.jpg"
        print("inside link")
        if request.status_code == 200:
            try:
                with open(filename, 'wb') as image:
                    for chunk in request:
                        image.write(chunk)
            except:
                return discord.Embed(description="The attachment is not an image :(", color=0xbf000a)
            try:
                api.update_with_media(filename, status=message)
                print("message sent")
                os.remove(filename)
            except:
                return discord.Embed(description="Picture size too big :(", color=0xbf000a)
    else:
        api.update_status(message)
        print("message sent")


bot.run(DISCORD_BOT_TOKEN)
