import tweepy
from time import sleep
from random import randint 

consumer_key = "QvPyBLxlIFMi5bQJ8FEtUyiSd" 
consumer_secret = "8ayGe7kd2qLFo8ffU1WXbJ5UEGBIZDuGIVk1jwluLxWgCBOwCK"     
access_token = "1250597054302355456-mv5EtZUh8RCLnvjmv6TVupD5k3bIid"     
access_token_secret = "AxrdOT5tShF3ZXvVtomgPybdYMZek0UC1A9OnehJdZygI"

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
