def main():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)  # create an API object

    api.update_status("Hello , world. Just a reminder to tweet at me for codes and to tweet pictures of your receipts at me to keep me alive!")
main()
