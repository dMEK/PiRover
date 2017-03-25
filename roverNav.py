# This is the basic script described in the Make book
# The code has no Autonomy, it just takes instruction from and 
# transmits data to the user
# the sections of this code are based on the scripts in Motors and Sensors
# And should be suitabel foundation pieces for autonomy

import time
import os # python os module allows for interface with underying os on pi
import RPi.GPIO as GPIO
import subprocess # https://pymotw.com/2/subprocess/ provides consistent interface for 
                  # creating and working with additional processes - replases some of os module
from sht1x.Sht1x import Sht1x as SHT1x
import smbus
import math
from gps import *
import threading
from Adafruit_BMP085 import BMP085

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Motor setup
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

def rForward():
  
  "motor forward"
  GPIO.output(en, 1)
  GPIO.output(in1, 0)
  GPIO.output(in2, 1)
  
def lForward():
  "motor forward"
  GPIO.output(en, 1)
  GPIO.output(in3, 0)
  GPIO.output(in4, 1)
  
def rBackward():
  "motor backward"
  GPIO.output(en, 1)
  GPIO.output(in1, 1)
  GPIO.output(in2, 0)

def lBackward():
  "motor backward"
  GPIO.output(en, 1)
  GPIO.output(in3, 1)
  GPIO.output(in4, 0)

def allStop:
  GPIO.output(enA, 0)
  GPIO.output(enB, 0)

def forward():
  lForward()
  rForward()

def reverse():
  rBackward()
  lBackward()
  
def spinRight():
  lForward()
  rBackward()
  
def spinLeft():
  rForward()
  lBackward()
  
# GPS Setup
gpsd = None

class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd
    gpsd = gps(mode=WATCH_ENABLE)
    self.current_value = None
    self.running = True
    
  def run(self):
    global gpsd
    while gpsd.running:
      gpsd.next()
      
# Compass setup

