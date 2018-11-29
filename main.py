import RPi.GPIO as GPIO
import time
import datetime
import json
import sound_direction as direct
import database_code

#GPIO SETUP
channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

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

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
        time.sleep(1)
