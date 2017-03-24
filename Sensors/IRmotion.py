# simple script for IR motion sensor
# the one used in the example is the Parallax RB-Plx-75
# it outputs a high signal when a change in IR signatures is detected
# attach a resistor and the LED anode(+) to pin 13, which will switch on when motion is detected


import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(13, GPIO.OUT)

while True:
  if GPIO.input (11):
    GPIO.output (13, 1)
  else:
    GPIO.output (13, 0)
