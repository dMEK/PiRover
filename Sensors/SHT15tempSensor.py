# this code needs the spiSht1x library by Luca Nobili
# This library should be installed with the robot code directory
# The library should be named rpiSht1x-1.2.tar.gz

fromsht1x.Sht1x import Sht1x as SHT1x

dataPin = 11
clkPin = 7

sht1x = SHT1x(dataPin, clkPin, SHT1x.GPIO_BOARD)

temperature = sht1x.read_temperature_C()
humidity = sht1x.read_humidity()
dewPoint = sht1x.calculate_dew_point(temperature, humidity)

print ("Temperature: {} Humidity: {} Dew Point: {}".format(temperature, humidity, dewPoint))
