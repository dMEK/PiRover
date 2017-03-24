# sample code for using a photo resistor with the rasp Pi
# For analog devices and the Pi, an ADC is needed
# this example originally used the MCP3008 - 8ch 10 bit
# this chip uses the SPI bus
#it uses the SPI python wrapper py-spidev, which should be installed in the robot main directory


import time
import spidev

spi = spidev.Spidev()
spiopen(0, 0)

def readChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data
  
while True:
  lightlevel = readChannel(0)
  print "Light level: " + str(readChannel(0))
  time.sleep(1)
