# This is code to use the HMC5883L compass
# it uses i2c communication - so needs the Serial Management Bus library smbus

import smbus
import math

bus = smbus.SMBus(0)
address = 0x1e
pi = math.pi

def read_byte(adr):
  return bus.read_byte_data(address, adr)

def read_word(adr):
  high = bus.read_byte_data(address, adr)
  low = bus.read_byte_data(address, adr + 1)
  val = (high << 8) + low
  return val

def read_word_2c(adr):
  val = read_word(adr)
  if val >= 0x8000:
    return -((65535 - val) + 1)
  else:
    return val
  
def write_byte(adr, value):
  bus.write_byte_data(address, adr, value)

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
print "Bearing: ", math.degrees(bearing)
