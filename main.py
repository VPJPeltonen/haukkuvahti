import RPi.GPIO as GPIO
import time
import datetime
#import json
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

#checked stuff
a_check = False
b_check = False
c_check = False

def insert_data(time1,time2,time3):
        time = datetime.datetime.now()
        #direction = direct.tempdirection() 
        direction = direct.direction(time1,time2,time3)
        data = [time,direction] 
        database_code.add_bark(data)      
        print(data)

def callback_a(self):
        stamp = time.time()
        print('callback a')
        global timeA 
        timeA = stamp

def callback_b(self):
        stamp = time.time()
        print('callback b')
        global timeB 
        timeB = stamp
def callback_c(self):
        stamp = time.time()
        print('callback c')
        global timeC 
        timeC = stamp

GPIO.add_event_detect(channel_a, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_detect(channel_b, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_detect(channel_c, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW

GPIO.add_event_callback(channel_a, callback_a)  # assign function to GPIO PIN, Run function on change

GPIO.add_event_callback(channel_b, callback_b)  # assign function to GPIO PIN, Run function on change

GPIO.add_event_callback(channel_c,callback_c)  # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
        time.sleep(1)
        if timeA != 0 and timeB != 0 and timeC != 0:
                insert_data(timeA,timeB,timeC)
                timeA = 0
                timeB = 0
                timeC = 0
        print ('test')
