import tweepy
import datetime
import time
import random
import markovify
import pytz


#consumer_token, consumer_secret
auth = tweepy.OAuthHandler("RVKCnjsVumv5IYlusASw11eeS", "n3SwC4uMgX2ZVEzRapYJZPQgohBKrGIXhCW1W50SFvoDmsZiPM")
#key, secret
auth.set_access_token("937031523546656769-ghkofIHf0fB01tMnblF2TQHFrtsQRv2", "buQyBSKtdaUsfdZ3Rfq4gPvnfIRCcPCESLtZQMXF8px7o")

api = tweepy.API(auth)
query_list = open('buzzwords.txt').read().splitlines()



with open("motivational_quotes.txt") as f:
    text = f.read()

text_model = markovify.Text(text, state_size=2)


while True:
	sent_Tweet=False
	bad_retweet=0
	if 8 < datetime.datetime.now(pytz.timezone('US/Eastern')).hour < 18:
		randomNow = random.random()
		if randomNow > .25 and bad_retweet < 2:
			while not sent_Tweet:
                                try:
					buzzword = random.choice(query_list)
					print "Random buzzword is '" + buzzword + "'"
					retweetlist = api.search(q=buzzword, lang="en")
					newesttweet = retweetlist[0].id
					print "Retweeting " + retweetlist[0].text.encode('UTF-8')
					api.retweet(newesttweet)
					sent_Tweet = True
					randomInterval = random.randint(600,4200)
					print "Sleeping " + str(randomInterval) + " seconds"
					time.sleep(randomInterval)
                                except:
					++bad_retweet
					print "Bad retweet. Skipping"""
		else:
			while not sent_Tweet:
				try:
					tweetToTweet = text_model.make_sentence()
					print "Tweeting " + tweetToTweet
					api.update_status(status=tweetToTweet)
					sent_Tweet = True
					randomInterval = random.randint(600,4200)
					print "Sleeping " + str(randomInterval) + " seconds"
					time.sleep(randomInterval)
				except:
					print "Bad tweet. Skipping"

	else:
		print "I'm asleep now because I'm a working man. Sleeping 2000 seconds to check if it's morning."
		time.sleep(2000)
