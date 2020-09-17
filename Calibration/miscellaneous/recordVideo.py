# recording.py
from picamera import PiCamera
import time

camera = PiCamera()
camera.vflip = True
#camera.start_preview()
camera.framerate = 32
camera.start_recording("cal.h264")
camera.wait_recording(60)
camera.stop_recording()
#camera.stop_preview()