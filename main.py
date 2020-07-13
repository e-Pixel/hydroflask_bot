import tweepy
from time import sleep # delay 
from datetime import datetime
import random
import os 
import calendar

print("Beginning...!")

consumer_key = None
consumer_secret = None
access_token = None
access_token_secret = None

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth) # insert authorization
public_tweets = api.home_timeline() # a copy of the timeline in my twitter account (completely optional)

nowZone = datetime.now()
newMessage = r"Today is {1} {0}, {2} ... Don't forget to stay hydrated!".format(str(nowZone.day), calendar.month_name[nowZone.month], str(nowZone.year))
# Today is MONTH DAY, YEAR ... Don{t forget to stay hydrated!

def getRandomPicture(): # getting random picture from directory 
    chooseRandomElement = random.choice(os.listdir("imagenes/"))
    print(chooseRandomElement)
    return "imagenes/" + chooseRandomElement

while True: # making everything
    value = getRandomPicture()
    api.update_with_media(getRandomPicture(),status=newMessage)
    sleep(86400) # an hour has 3600 seconds
    # a day has 86400 seconds
