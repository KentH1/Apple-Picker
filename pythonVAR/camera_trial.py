from picamera import PiCamera
from time import sleep

camera=PiCamera()
camera.resolution = (2592, 1944)
camera.framerate=15
camera.rotation=180
camera.start_preview(fullscreen=False,window=(100,200,300,400))
#for i in range(3):
  #  sleep(5)
 #   camera.capture('/home/pi/Desktop/image%s.jpg' % i)
sleep(10)
camera.capture('/home/pi/Desktop/image1.jpg')
camera.stop_preview()



