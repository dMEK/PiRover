# This is a console driven servo position mapping program
# It uses the ServoBlaster library by Richard Hirst
# ServoBlaster helps smooth servo motion on the Pi
# Syntax is echo (servo=value) > /dev/servoblaster in linux terminal
# Or call("echo (servo=value) > /dev/servoblaster" , shell=True)

from subprocess import call
import time

while True:
  position = raw_input("Enter servo value: ")
  call("echo 2=" + position + " > /dev/servoblaster" , shell=True)
  time.sleep(2)
