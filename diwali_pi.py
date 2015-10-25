import time
import RPi.GPIO as GPIO
from twython import TwythonStreamer
import os
import random
# Search terms
TERMS = '#Diwali'

# GPIO pin number of LED
LED = 22

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
				tweetlen=len(tweetstring)
				print tweetlen
				tone=random.randrange(1,7)
				tone_str=str(tone)
				play_str="aplay "+tone_str+".wav"
				os.system(play_str)
				if(tweetlen<50):
					tweetlen=10
				else:
					tweetlen=30
				GPIO.output(LED,GPIO.HIGH)
				time.sleep(random.randrange(1,tweetlen)/5)
				GPIO.output(LED,GPIO.LOW)
				time.sleep(random.randrange(1,tweetlen)/5)
				GPIO.output(LED,GPIO.HIGH)
				time.sleep(random.randrange(1,tweetlen)/5)
				GPIO.output(LED,GPIO.LOW)
				time.sleep(random.randrange(1,tweetlen)/5)
				GPIO.output(LED,GPIO.HIGH)
				time.sleep(random.randrange(1,tweetlen)/5)
				GPIO.output(LED,GPIO.LOW)
				time.sleep(random.randrange(1,tweetlen)/5)
				GPIO.output(LED,GPIO.HIGH)
				time.sleep(random.randrange(1,tweetlen)/5)
				GPIO.output(LED,GPIO.LOW)
				time.sleep(random.randrange(1,tweetlen)/5)
				GPIO.output(LED,GPIO.HIGH)	


# Setup GPIO as output
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

# Create streamer
try:
        stream = DiwaliStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        stream.statuses.filter(track=TERMS)
except KeyboardInterrupt:
        GPIO.cleanup()

