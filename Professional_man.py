import tweepy
import datetime
import time
import random
import markovify


auth = tweepy.OAuthHandler("oWy8QTMkNcmJbTXoSXayV5TwX", "CXuNf84gGANCbgZMVidLpP84sm76rvvE7ybLbjd0Ssm8kh0Cjl")
auth.set_access_token("937031523546656769-VOOIfMebro9ppkATsqKzn1nIS6bpsHp", "pnzXBEFbXW1Z2Cv3xm2wdd11knVXjUgptiQQnBHMFda00")

api = tweepy.API(auth)
query_list = open('buzzwords.txt').read().splitlines()

with open("motivational_quotes.txt") as f:
    text = f.read()

text_model = markovify.Text(text, state_size=2)

while True:
	sent_Tweet=False
	if 8 < datetime.datetime.now().hour < 21:
		randomNow = random.random()
		if randomNow > .25:
			while not sent_Tweet:
				try:
					buzzword = random.choice(query_list)
					retweetlist = api.search(q=buzzword)
					newesttweet = retweetlist[0].id
					api.retweet(newesttweet)
					sent_Tweet = True
					print "retweeted " + retweetlist[0].text.encode('UTF-8')
					print "sleeping 15 seconds"
					time.sleep(30)
				except: 
					print "Bad retweet. Skipping"
		else:
			while not sent_Tweet:
				try:
					tweetToTweet = text_model.make_sentence()
					print "tweeting " + tweetToTweet
					api.update_status(status=tweetToTweet)
					sent_Tweet = True
					print "sleeping 15 seconds"
					time.sleep(30)
				except:
					print "Bad tweet. Skipping"

	else:
		print "I'm asleep now because I'm a working man. Sleeping 2000 seconds to check if it's morning."
		time.sleep(2000)

"""searched_tweets = api.search(q="test")
for tweet in searched_tweets:
	if 8 < datetime.datetime.now().hour < 20:
		try:
			print(tweet[0].text)
		except: pass
	else:
		print "waiting"
		time.sleep(10000)"""