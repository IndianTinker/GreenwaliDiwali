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
APP_KEY = 'j2lUkuWFfdUTlopxGmkPcrmYE'
APP_SECRET = 'qaOkHjomIJGtfsgDWIGMJ7a1vhgY9oB2zRWN2PyKRmM0bVbOsp'
OAUTH_TOKEN = '1610388554-wcneXN2e9IB8wJ7oYQudCHzjc1APtDvQLdsfLtK'
OAUTH_TOKEN_SECRET = 'nk1sNDltROEYj2iszKQafSH17iLEnRZm9gZtSWgE5pdTI'

# Setup callbacks from Twython Streamer
class DiwaliStreamer(TwythonStreamer):
        def on_success(self, data):
                if 'text' in data:
                        tweetstring=data['text'].encode('utf-8')
			print tweetstring
			tweetlen=len(tweetstring)
			if(tweetlen<50):
				tweetlen=1
			else:
				tweetlen=2
			GPIO.output(LED,GPIO.HIGH)
			time.sleep(random.randrange(0.1,tweetlen,0.5))
			GPIO.output(LED,GPIO.LOW)
			time.sleep(random.randrange(0.1,tweetlen,0.5))
			GPIO.output(LED,GPIO.HIGH)
			time.sleep(random.randrange(0.1,tweetlen,0.5))
			GPIO.output(LED,GPIO.LOW)
			time.sleep(random.randrange(0.1,tweetlen,0.5))
			GPIO.output(LED,GPIO.HIGH)
			time.sleep(random.randrange(0.1,tweetlen,0.5))
			GPIO.output(LED,GPIO.LOW)
			time.sleep(random.randrange(0.1,tweetlen,0.5))
			GPIO.output(LED,GPIO.HIGH)
			time.sleep(random.randrange(0.1,tweetlen,0.5))
			GPIO.output(LED,GPIO.LOW)
			time.sleep(random.randrange(0.1,tweetlen,0.5))	
			GPIO.output(LED.GPIO.HIGH)		
			if ((tweetstring.find("green")+1) or (tweetstring.find("Green")+1)):
				tone=random.randrange(1,7)
				tone_str=str(tone)
				play_str="aplay "+tone_str+".wav"
				os.system(play_str)

# Setup GPIO as output
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

# Create streamer
try:
        stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        stream.statuses.filter(track=TERMS)
except KeyboardInterrupt:
        GPIO.cleanup()

