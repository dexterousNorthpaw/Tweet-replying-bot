#this is tweet replying bot

import tweepy #library used to access the API
import time

print("This is my twitter bot")

#keys are to be here
CONSUMER_KEY= ''
CONSUMER_SECRET= ''
ACCESS_KEY = ''
ACCESS_SCRET =''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SCRET)
api = tweepy.API(auth)

filename ="lastSeen_id.txt" #file to store ID of tweets

def get_last_id(file_name): #accessing the last ID saved in the file
    f_read = open(file_name, 'r')
    lastSeen_id = (f_read.read().strip())
    f_read.close()
    return lastSeen_id

def save_last_id(lastSeen_id, file_name): #to save last ID of tweet
    f_write = open(file_name, 'w')
    f_write.write(str(lastSeen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('getting and replying to tweets...')
    lastSeen_id = get_last_id(filename)
    mentions = api.mentions_timeline(lastSeen_id, tweet_mode='extended') #all mentions in the account

    for mention in reversed(mentions):
        print(str(mention.id) + " - " + mention.full_text)
        lastSeen_id = mention.id
        save_last_id(lastSeen_id, filename)
        if "follow" in mention.full_text.lower():
            print("keyword found")
            print('responding...')
            api.update_status('@' + mention.user.screen_name + ' Hello Human... thanks for testing', mention.id)



while True:
    reply_to_tweets()
    time.sleep(5)
