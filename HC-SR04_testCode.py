# sample code for use with the HC-SR04 Ultrasonic range finder sensor
# HC-SR04 outputs a 5V signal, a 1K resistor should be put on the input pin to pull down the voltage
# and avoid damage to the Pi

import RPi.GPIO as GPIO
import time

trig = 23
echo = 24

GPIO.setmode(GPIO.BCM)

def read_distance():
  GPIO.output(trig, True)
  time.sleep(0.005)
  GPIO.output(trig, False)
  
  while GPIO.input(echo) == 0:
    signaloff = time.time()
    
  while GPIO.input(echo) == 1:
    signalon = time.time()
    
  timepassed = signalon - signaloff
  distanceCM = timepassed * 17000 #converts signal delay into CM
  return distanceCM
  
while True:
  print "Distance: %f cm" %read_distance()
