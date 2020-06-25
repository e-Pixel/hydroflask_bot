import tweepy
from time import sleep
from random import randint 
import setup

consumer_key = environ['consumer_key'] 
consumer_secret = environ['consumer_secret']  
access_token = environ['access_token'] 
access_token_secret = environ['access_token_secret'] 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth) # insert authorization
public_tweets = api.home_timeline() # a copy of the timeline in my twitter account

print(public_tweets)

hydr_message = "Don't forget to drink water and stay hydrated!"
hydr_img = 'turtles.jpg'
hydr_list = ["turtles.jpg","01.jpg"]

def getRandomPicture(): # refresh everytime 
	randomNumber = randint(0,len(hydr_list)-1)
	return randomNumber

while True:
	value = getRandomPicture()
	api.update_with_media(hydr_list[value],status=hydr_message)
	sleep(3600) # an hour has 3600 seconds
