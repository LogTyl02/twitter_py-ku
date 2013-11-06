import json

from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream
import tweepy
f = open('inTweet.txt', 'r+')

consumer_key="9Bva6LvQVPUMGmjALRcNw"
consumer_secret="sAeXGJyCRbPEGZMe8uIUNHXJiy7W2b8TApjSbowODc"

access_token="2171077380-mE6EhzcahlDkwA4aPsIgpBkVd1YbG6Wqlu8S1Ja"
access_token_secret="u3BbVM2tOi01ZDVx76djk7AUj0AdHGrA7cXDNeqbNMx9N"

class StdOutListener(StreamListener):	

	#def on_data(self, data):
		print data['text']
		json.dumps(data['text'], f)
		return False

	def on_status(self, status):
		print status
		return False

	def on_error(self, status):
		print 'error ' + str(status)
		return False


if __name__ == '__main__':
	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	
 	stream = Stream(auth, l)
	#stream.filter(track=['winter'])

	stream.sample()


	
		
