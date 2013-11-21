import json
import tempfile

from file_handler import *

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

	def on_data(self, raw_data):
		data = json.loads(raw_data)
		#print data
		if len(data) < 23:
			print 'Donk'
			stream.disconnect()
		else:
			if data['lang'] == 'en':
				print data['text']
			else:
				print 'Nope'
		stream.disconnect()

	def on_status(self, status):
		print status
		

	def on_error(self, status):
		print 'error ' + str(status)


if __name__ == '__main__':
	output_handler = FileHandler('poem.txt', 'r', 'output.txt', 'r+') 		# Making an object to deal with file i/o

	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	
 	stream = Stream(auth, l)
	#stream.filter(track=['bunny'])
	stream.disconnect()
	stream.sample()
	stream.disconnect()