import tweepy
from secrets import *
import os
import random


def blacklist(tweet):
    file = open('/home/pi/Desktop/twitterBot/FreedomFries/TwitterBot/replied.txt', 'a')
    file.write(tweet + "\n")
    file.close()


def searchTweet(api, searchTerm):
    searchResults = [status for status in tweepy.Cursor(api.search, q=searchTerm).items(100)]
    return searchResults


def read_codes(path):
    #'/home/pi/Desktop/twitterBot/FreedomFries/TwitterBot/testfile.txt'
    codes = []
    with open(path) as f:
        for line in f:
            temp = line
            temp = temp.strip()
            codes.append(temp)
            if 'str' in line:
                break
    return codes


def find_mentions(api):
    mentions = [status for status in tweepy.Cursor(api.search, q="@FreedomFries16", include_entities=True).items(10)]
    print(len(mentions))

    print(mentions[0].id)

def add_user_to_file(user_info, path):
    with open(path, 'a') as f:
        id = user_info[0]
        name = user_info[1]
        f.write(str(id)+","+name+"\n")


def write_codes_to_file(codes, path):
    with open(path, 'w') as f:
        for code in codes:
            f.write(str(code)+"\n")


def size(file):
    return os.stat(file).st_size


def read_in_blacklist(blacklist_path):
    blacklist = []
    if (size(blacklist_path) > 0):
        with open(blacklist_path) as f:
            str = f.readlines()
            for s in str:
                blacklist.append([int(s.strip().split(",")[0]), s.strip().split(",")[1]])
    return blacklist

def reply_to_mentions(api, blacklist_path, code_path):
    # Read in list of users that have already been tweeted at  form: [[user_id, screen_name],[....]]
    blacklist = read_in_blacklist(blacklist_path)

    # loop through all mentions
    codes = read_codes(code_path)
    mentions = [status for status in tweepy.Cursor(api.search, q="@FreedomFries16", include_entities=True).items(10)]
    for m in mentions:
        tweet_id = m.id
        user = m.user
        user_info = [user.id, user.screen_name]

        # if user is not in blacklist and has tweeted media then reply
        # To reply to only pictures use: m.entities.get('media') is not None
        if (user_info not in blacklist):
            # get random code
            to_use = random.randint(0, len(codes))
            code_to_send = codes[to_use]
            # remove code from list
            codes.remove(code_to_send)
            # Reply to user
            status = "@"+user_info[1]+" "+code_to_send+" Use this code for a free medium fry!"
            api.update_status(status, in_reply_to_status_id = tweet_id)
            # Append user to file
            add_user_to_file(user_info, blacklist_path)

    # Re-write codes to file
    write_codes_to_file(codes, code_path)


def main():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)  # create an API object
    blacklist_path = "/home/pi/Desktop/twitterBot/FreedomFries/TwitterBot/blacklist.txt"
    code_path = "/home/pi/Desktop/twitterBot/FreedomFries/TwitterBot/testfile.txt"
    reply_to_mentions(api, blacklist_path, code_path)

main()
