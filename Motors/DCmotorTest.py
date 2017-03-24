# this is a simple test code for use with 2 DC motors 
# and a simple H bridge board such as the L298H
# This code provides only direction but no speed control


import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# motor controller pins for motor A - Right

in1 = 19 # input 1 to pin 19
enA = 21 # enable A to pin 21
in2 = 23 # input 2 to pin 23

# motor controller pins for motor B - Left

in3 = 22
enB = 24
in4 = 26

GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(enA, GPIO.OUT)
GPIO.setup(enB, GPIO.OUT)

def rForward()
  "motor forward"
  GPIO.output(en, 1)
  GPIO.output(in1, 0)
  GPIO.output(in2, 1)
  
def lForward()
  "motor forward"
  GPIO.output(en, 1)
  GPIO.output(in3, 0)
  GPIO.output(in4, 1)
  
def rBackward()
  "motor backward"
  GPIO.output(en, 1)
  GPIO.output(in1, 1)
  GPIO.output(in2, 0)

def lBackward()
  "motor backward"
  GPIO.output(en, 1)
  GPIO.output(in3, 1)
  GPIO.output(in4, 0)

def allStop
  GPIO.output(enA, 0)
  GPIO.output(enB, 0)

rForward()
lForward()
time.sleep(2)
allStop()
time.sleep(0.5)
rBackwards()
lBackwards()
time.sleep(2)
allStop()
