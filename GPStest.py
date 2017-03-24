# for a UART connected GPS, edit the arguments for terminal communication from the cmdline.txt file
# and edit the inittab file to comment out the terminal connection line
# this program polls the GPS position every 30 seconds and saves it to locations.csv in the currewnt directory


from gps import *
import time
import threading

f = open("locations.csv", "w")

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
      
if __name__ == '__main__':
  gpsp = GpsPoller()
  try:
    gpsp.start()
    while True:
      f.write(str(gpsd.fix.longitude)
      + "," + str(gpsd.fix.latitude)
      + "\n")
      time.sleep(30)
  except(KeyboardInterrupt, SystemExit):
    f.close()
    gpsp.running = False
    gpsp.join()
