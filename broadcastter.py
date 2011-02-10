import tweepy
import yaml
import csv
import time

str = open('appdetail.yaml').read()
appdetail = yaml.load(str)
auth = tweepy.OAuthHandler(appdetail['consumer_key'], appdetail['consumer_secret'])
auth.set_access_token(appdetail['access_key'], appdetail['access_secret'])  
api = tweepy.API(auth)
filename = 'namelist.csv'
csvfile = open(filename)
for row in csv.reader(csvfile):
    for screen_name in row:
        api.update_status("@" + screen_name + " " + "hello")
        time.sleep(10)
print 'sent mentions'
