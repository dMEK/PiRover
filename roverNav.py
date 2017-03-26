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

def allStop():
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
bus = smbus.SMBus(0)
compAddress = 0x1e
pi = math.pi

def read_byte(adr):
  return bus.read_byte_data(compAddress, adr)

def read_word(adr):
  high = bus.read_byte_data(compAddress, adr)
  low = bus.read_byte_data(compAddress, adr + 1)
  val = (high << 8) + low
  return val

def read_word_2c(adr):
  val = read_word(adr)
  if val >= 0x8000:
    return -((65535 - val) + 1)
  else:
    return val
  
def write_byte(adr, value):
  bus.write_byte_data(compAddress, adr, value)
  
def getBearing():
  #write 112, 32 and 0 to the device to config for reading
  write_byte (0, 0b01110000)
  write_byte (1, 0b00100000)
  write_byte (1, 0b00000000)

  # offset values need to be callibrated to postion on the planet
  scale = 0.92
  x_offset = -39
  y_offset = -100

  x_out = (read_word_2c(3) - x_offset) * scale
  y_out = (read_word_2c(7) - y_offset) * scale

  bearing = math.atan2(y_out, x_out)
  if bearing < 0:
    bearing += 2 * pi
  return str(math.degrees(bearing))

#Robot Arm Servo

loR = 40
hiR = 100
smth = 0.5 #delay to smooth servo motion

def raise_arm():
  for i in range (loR, hiR):
  call("echo 2=" + str(i) + " > /dev/servoblaster" , shell=True)
  time.sleep(smth)
  
def lower_arm():
  for i in reversed(range (loR, hiR)):
  call("echo 2=" + str(i) + " > /dev/servoblaster" , shell=True)
  time.sleep(smth)
  
#Rangefinder Setup

trig = 15
echo = 13

GPIO.setup(trig, OUT)
GPIO.setup(echo, IN)

def getRange():
  time.sleep(0.3)
  GPIO.output(trig, True)
  time.sleep(0.00001)
  GPIO.output(trig, False)
  
  while GPIO.input(echo) == 0:
    signaloff = time.time()
    
  while GPIO.input(echo) == 1:
    signalon = time.time()
    
  timepassed = signalon - signaloff
  distanceCM = timepassed * 17000 #converts signal delay into CM
  return str(distanceCM)

#Pressure and Temperature

bmp = BMP085(0x77)

def getTemp():
  return str(bmp.readTemperature())

def getPressure():
  return str(bmp.readPressure()/1000)

if __name__ = '__main__':
  isGPS = False
  gpsQuery = raw_input("Is GPS connected to this unit?").lower()
  if gpsQuery in ('y', 'yes'):
    isGPS = True
    gpsp = GpsPoller()
    gpsp.start()
  try:
    while True:
      
      # get command from user
      
      os.system("clear")
      
      print "Range to target: " + getRange()
      print "Temp: " + getTemperature() + "C"
      print "Pressure: " + getPressure() + "kPa"
      if isGPS:
        print "Location: " + str(gpsd.fix.longitude) + "," + str(gpsd.fix.latitude)
      print "Bearing: " + getBearing() + "degrees"
      print "W = Forward"
      print "S = Backward"
      print "A = Left"
      print "D = Right"
      print "Space = Stop"
      print "O = Raise Arm"
      print "K = Lower Arm"
      print "P = Take Picture"
      
      command = raw_input("Enter Command (Q to Quit): ").lower()
      
      if command =="w":
        forward()
        time.sleep(0.5)
        continue
      elif command =="s":
        reverse()
        time.sleep(0.5)
        continue
      elif command =="a":
        spinLeft()
        time.sleep(0.5)
        continue
      elif command =="d":
        spinRight()
        time.sleep(0.5)
        continue
      elif command ==" ":
        allStop()
        time.sleep(0.5)
        continue
      elif command =="o":
        raise_arm()
        time.sleep(0.5)
        continue
      elif command =="k":
        lower_arm()
        time.sleep(0.5)
        continue
      elif command =="p":
        subprocess.call("raspistill -o image.jpg, shell = True)
        time.sleep(0.5)
        continue
                        
      elif command =="q":
        if isGPS:
          gpsp.running = False
          gpsp.join()
        GPIO.cleanup()
        break
      
      else:
        print "Invalid Command"
        time.sleep(0.5)
        continue

  except (KeyboardInterrupt, SystemExit):
    if isGPS:
      gpsp.running = False
      gpsp.join()
    GPIO.cleanup()
      
      

 
