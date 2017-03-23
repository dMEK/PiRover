# this is a simple control and test code for running a servo on the Raspberry Pi
# it relies on RPi.GPIO and the ServoBlaster Library
# RPi.GPIO is included on recent distributions of Raspbian
# from the rover directory:
# wget https://raw.githubusercontent.com/richardghirst/PiBits/master/ServoBlaster/user/servod.c
# wget https://raw.githubusercontent.com/richardghirst/PiBits/master/ServoBlaster/user/Makefile
# make servod
# it runs as a background operation, to start type sudo ./servod

import RPi.GPIO as GPIO
import time

#this sets the numbering system for the board pins
GPIO.setmode (GPIO.BOARD)

 #sets pin 11 as the output
GPIO.setup (11, GPIO.OUT)

#sets pin 11's frquency at 50hz - pulse length 20ms
p = GPIO.PWM (11, 50) 

#sets the duty cycle at 7.5% or 1500 us - centred on most hobby servos
p.start (7.5) 

# a sweep test: duty cycle 11% = 2200us, duty cycle 3% = 600us
while True:
  p.ChangeDutyCycle (7.5)
  time.sleep (1)
  p.ChangeDutyCycle (11)
  time.sleep (1)
  p.ChangeDutyCycle (3)
  time.sleep (1)
  
GPIO.cleanup() #releases GPIO resources
