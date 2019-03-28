import tweepy
from secrets import *
import os
import random

codes = []
replied = []


def fillReplied():
    with open('replied.txt') as f:
        for line in f:
            temp = line
            temp = temp.strip()
            replied.append(temp)
            if 'str' in line:
                break


def blacklist(tweet):
    file = open('/home/pi/Desktop/twitterBot/FreedomFries/TwitterBot/replied.txt', 'a')
    file.write(tweet + "\n")
    file.close()


def searchTweet(api, searchTerm):
    searchResults = [status for status in tweepy.Cursor(api.search, q=searchTerm).items(100)]
    return searchResults


def tweet(api, text):
    twts = searchTweet(api, "\"@FreedomFries16\"")
    t = ['@FreedomFries16',
         'freedomfries16',
         'Freedomfries16',
         '@freedomFires16',
         'fry',
         'Free fries',
         'fries',
         'free fry',
         'free mcdonalds']
    for s in twts:
        user = s.user
        uid = s.id_str
        tid = s.id_str
        for i in t:
            if i in s.text:
                for reply in replied:
                    if tid not in replied:
                        blacklist(tid)
                        if uid != "1108539513834536961": #our own id
                            # print(s.text)
                            sn = s.user.screen_name
                            # print(sn)
                            m = "@" + sn + " " + text + " Use this code for a free medium fry!"
                            s = api.update_status(m, s.id)
                            print(m)

def rem_from_file(code):
    file = open('/home/pi/Desktop/twitterBot/FreedomFries/TwitterBot/testfile.txt', 'w')
    for i in range(len(codes)):
        if (i == code):
            temp = "do nothing"
        else:
            file.write(codes[i] + "\n")
    file.close()


def readCodes():
    with open('/home/pi/Desktop/twitterBot/FreedomFries/TwitterBot/testfile.txt') as f:
        for line in f:
            temp = line
            temp = temp.strip()
            codes.append(temp)
            if 'str' in line:
                break


def find_mentions(api):
    mentions = [status for status in tweepy.Cursor(api.search, q="@FreedomFries16", include_entities=True).items(10)]
    print(len(mentions))

    print(mentions[0].user.screen_name)


def reply_to_mentions(api):
    #TODO READ IN A LIST OF USERS THAT HAVE BEEN REPLIED TO ALREADY
    mentions = [status for status in tweepy.Cursor(api.search, q="@FreedomFries16", include_entities=True).items(10)]
    for m in mentions:
        user = m.user
        uid = user.id
        uname = user.screen_name

        #Check that user hasn't already been tweeted at today here
        #
        #

        if (m.entities.get('media') is not None):
            # Reply to user with code
            continue




def main():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)  # create an API object
    find_mentions(api)
    # readCodes()
    # fillReplied()
    # code = random.randint(0, len(codes))
    # tweet_code = codes[code]
    # tweet(api, tweet_code)
    # rem_from_file(code)
    # print("finished")
main()
