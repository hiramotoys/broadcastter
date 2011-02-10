import tweepy
import yaml

str = open('appdetail.yaml').read()
appdetail = yaml.load(str)
auth = tweepy.OAuthHandler(appdetail['consumer_key'], appdetail['consumer_secret'])
auth.set_access_token(appdetail['access_key'], appdetail['access_secret'])  
api = tweepy.API(auth)

