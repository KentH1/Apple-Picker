from picamera import PiCamera
from time import sleep

camera = PiCamera()
#camera.resolution = (2592, 1944)
#camera.framerate=15
camera.rotation=180
#camera.start_preview()
#sleep(50)
#camera.capture('/home/pi/Desktop/imageHighRes.jpg')
#camera.stop_preview()
camera.start_preview()
for i in range(100):
    camera.annotate_text = "Brightness: %s" % i + " Contrast: %s" % i
    camera.brightness = i
    sleep(0.1)
camera.stop_preview()