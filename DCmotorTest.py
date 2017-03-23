import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# motor controller pins for motor A

in1 = 19 # input 1 to pin 19
enA = 21 # enable A to pin 21
in2 = 23 # input 2 to pin 23

# motor controller pins for motor B

in3 = 22
enB = 24
in4 = 26

GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(enA, GPIO.OUT)
GPIO.setup(enB, GPIO.OUT)

def Forward()
  "motor forward"
  GPIO.output(en, 1)
  GPIO.output(in, )
  GPIO.output(in, )
  
def Forward()
  "motor forward"
  GPIO.output(en, 1)
  GPIO.output(in, )
  GPIO.output(in, )
  
def Backward()
  "motor backward"
  GPIO.output(en, 1)
  GPIO.output(in, )
  GPIO.output(in, )

def Backward()
  "motor backward"
  GPIO.output(en, 1)
  GPIO.output(in, )
  GPIO.output(in, )

def allStop
  GPIO.output(enA, 0)
  GPIO.output(enB, 0)
