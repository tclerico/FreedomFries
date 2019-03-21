import tweepy
from secrets import *
import os


def main():
    '''
    @Tim: bot can tweet, will share credentials and secret files with you
    going to automate with a crontab when we're ready
    '''
    #create an OAuthHandler instance
    # Twitter requires all requests to use OAuth for authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    auth.set_access_token(access_token, access_secret)

     #Construct the API instance
    api = tweepy.API(auth) # create an API object
    public_tweets = api.home_timeline()
    # for tweet in public_tweets:
    #     print(tweet.text)
    api.update_status('Learning how to speak!')
main()