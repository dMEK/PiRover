# simple sample code for a simple hall effct switch sensor
# this type of sensor either outputs a high or a low sig depending 
# on the presence of a magnetic field
#  pull_up_down = GPIO.PUD_DOWN sets the input pin to low when no input

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
prev_input = 0
while True:
  input = GPIO.input(11)
  if ((not prev_input) and input):
    print "Field changed."
  prev_input = input
  time_sleep(0.05)
  
