import tweepy

# OAuth setup
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

users = ["JoeBiden", "realDonaldTrump", "SenSanders", "VP"]

for username in users:
	user = api.get_user(username)

	user_timeline = api.user_timeline(user.id)
	tweets = []

	if (username == "JoeBiden" || username == "SenSanders"):
		ideology = "dem"
	else:
		ideology = "rep"


	for tweet in user_timeline:
		print("{")
	    print("\ttext: " + tweet + ",")
	    print("\tideology:" + ideology + ",")
	    print("\tauthor: " + username + ",")
	    print("\tisFallacy: false")
	    print("},")

