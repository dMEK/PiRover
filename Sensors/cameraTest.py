# uses the python-picamera library

import picamera
import time

#take a photo
camera = picamera.PiCamera()
camera.capture('image.jpg')

#make a 5s movie
camera.start_recording('video.h264')
time.sleep(5)
camera.stop_recording()
