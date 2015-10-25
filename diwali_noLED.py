#import time
#import RPi.GPIO as GPIO
from twython import TwythonStreamer
import os
import random
# Search terms
TERMS = '#Diwali'

# GPIO pin number of LED
#LED = 22

# Twitter application authentication
APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

# Setup callbacks from Twython Streamer
class DiwaliStreamer(TwythonStreamer):
        def on_success(self, data):
			if 'text' in data:
				tweetstring=data['text'].encode('utf-8')
				tweetstringl=tweetstring.lower()
				if ((tweetstringl.find("green")+1)):
					print tweetstring
					tone=random.randrange(1,7)
					tone_str=str(tone)
					play_str="aplay "+tone_str+".wav"
					os.system(play_str)

# Setup GPIO as output
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(LED, GPIO.OUT)
#GPIO.output(LED, GPIO.LOW)

# Create streamer
stream = DiwaliStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
stream.statuses.filter(track=TERMS)

