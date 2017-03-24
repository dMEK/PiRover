# Sample code for use with a Reed Switch
# bouncetime function is in ms, and is part of the GPIO lib

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_UP) #pin 11, high on open switch

def switch_closed(channel):
  print "Switch closed"
  
# This line is the interrupt
GPIO.add_event_detect(11, GPIO.FALLING, callback=switch_closed, bouncetime=300)

while True:
  time.sleep(10)
