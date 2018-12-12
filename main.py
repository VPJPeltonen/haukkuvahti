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

#times stuff
timeA = 0
timeB = 0
timeC = 0

def insert_data(time1,time2,time3):
        time = datetime.datetime.now()
        #direction = direct.tempdirection() 
        direction = direct.direction(time1,time2,time3)
        data = [time,direction] 
        database_code.add_bark(data)      
        print(data)

def callback_a(channel):
        timeA = time.time()
        print(timeA)
        return timeA

def callback():
        stamp = time.time()
        return stamp

def callback_b(channel):
        timeB = time.time()
        print('b noise')
        return timeB

def callback_c(channel):
        timeC = time.time()
        print('c noise')
        return timeC

def check(pin):
        return True

#GPIO.add_event_detect(channel_a, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
#GPIO.add_event_detect(channel_b, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
#GPIO.add_event_detect(channel_c, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW

timeA = GPIO.add_event_callback(channel_a, callback_a)  # assign function to GPIO PIN, Run function on change
a_checked = GPIO.add_event_callback(channel_a, check)  # assign function to GPIO PIN, Run function on change

timeB = GPIO.add_event_callback(channel_b, callback_b)  # assign function to GPIO PIN, Run function on change
b_checked = GPIO.add_event_callback(channel_b, check)  # assign function to GPIO PIN, Run function on change

timeC = GPIO.add_event_callback(channel_c, callback_c)  # assign function to GPIO PIN, Run function on change
c_checked = GPIO.add_event_callback(channel_c, check)  # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
        time.sleep(1)
        if a_checked and b_checked and c_checked:
                insert_data(timeA,timeB,timeC)
                print ('test')
                a_checked = False
                b_checked = False
                c_checked = False