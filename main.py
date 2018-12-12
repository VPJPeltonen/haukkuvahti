import RPi.GPIO as GPIO
import time
import datetime
import json
import sound_direction as direct
import database_code

#GPIO SETUP, all pins set up
channel_a = 4
channel_b = 17
channel_c = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel_a, GPIO.IN)
GPIO.setup(channel_b, GPIO.IN)
GPIO.setup(channel_c, GPIO.IN)

def oldcallback(channel):
        data = {}
        data['time'] = datetime.datetime.now()
        if GPIO.input(channel):
                data['volume'] = "Loud Sound"
        else:
                data['volume'] = "Sound"
        data['direction'] = direct.tempdirection()        
        json_data = json.dumps(data, indent=4, sort_keys=True, default=str)
        print(json_data)

def callback(channel):
        time = datetime.datetime.now()
        direction = direct.tempdirection() 
        data = [time,direction] 
        database_code.add_bark(data)      
        print(data)

def callback_a(channel):
        print('a noise')

def callback_b(channel):
        print('b noise')

def callback_c(channel):
        print('c noise')

GPIO.add_event_detect(channel_a, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_detect(channel_b, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_detect(channel_c, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel_a, callback_a)  # assign function to GPIO PIN, Run function on change
GPIO.add_event_callback(channel_b, callback_b)  # assign function to GPIO PIN, Run function on change
GPIO.add_event_callback(channel_c, callback_c)  # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
        time.sleep(1)
