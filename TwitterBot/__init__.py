import tweepy
from secrets import *
import os
import random
codes = []
def tweet(api, text):
    # public_tweets = api.home_timeline()
    # for tweet in public_tweets:
    #     print(tweet.text)
    api.update_status(text+" Use this code for a free medium fry!")


def rem_from_file(code):
    file = open('testfile.txt', 'w')
    for i in range(len(codes)):
        if(i==code):
            file.write("")
        else:
            file.write(codes[i] + "\n")
    file.close()

def readCodes():
    with open('testfile.txt') as f:
        for line in f:
            temp = line
            temp=temp.strip()
            codes.append(temp)
            if 'str' in line:
                break

def main():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth) # create an API object
    readCodes()
    code=random.randint(0,len(codes))
    tweet_code=codes[code]
    tweet(api,tweet_code)
    rem_from_file(code)
    print("finished")

main()