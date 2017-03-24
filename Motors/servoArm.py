# This is a console driven servo position mapping program
# It uses the ServoBlaster library by Richard Hirst
# ServoBlaster helps smooth servo motion on the Pi
# Syntax is echo (servo=value) > /dev/servoblaster in linux terminal
# Or call("echo (servo=value) > /dev/servoblaster" , shell=True)
# This code uses arbitrary high and low postion range of  40 and 100
# These should be determined using the Servo Test code

from subprocess import call
import time

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
