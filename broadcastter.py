import tweepy
import yaml
import csv
import time
import sys

L = 139
s = open('appdetail.yaml').read()
appdetail = yaml.load(s)
auth = tweepy.OAuthHandler(appdetail['consumer_key'], appdetail['consumer_secret'])
auth.set_access_token(appdetail['access_key'], appdetail['access_secret'])  
api = tweepy.API(auth)
text = unicode(raw_input('input text message: '), 'UTF-8')
textlength = len(text)
print 'input num', textlength
l = L - textlength
if l < 0 :
    print 'too long'
    sys.exit()
filename = 'namelist.csv'
csvfile = open(filename)
to_list = []
for row in csv.reader(csvfile):
    for screen_name in row:
        at_screen_name = "@" + screen_name + " "
        print at_screen_name
        to_list.append(at_screen_name)
grouped_to_list = [""] * len(to_list)
for to in to_list:
    for i in range(len(grouped_to_list)):
        if len(grouped_to_list[i] + to) < l:
            grouped_to_list[i] += to
            break
print grouped_to_list
for grouped_to in grouped_to_list:
    if grouped_to == "":
        break
    senttext = grouped_to + text
    api.update_status(senttext)
    print 'mention ' + senttext
    time.sleep(30)
print 'sent mentions'
