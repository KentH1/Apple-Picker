#Peripheral Definitions
print("Start Setup")
import RPi.GPIO_0_7_0 as GPIO
import time
GPIO.setmode(GPIO.BCM) #Sets reference to pins to be their GPIO __ number



#-----------Stepper-----------
from RpiMotorLib import RpiMotorLib

stepperPINS = [4,17,27,22] #[2B,2A,1A,1B]
#for pin in stepperPINS:
#  GPIO.setup(pin, GPIO.OUT)
#  GPIO.output(pin, 0)

halfstep_seq = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]
#-----------Laser Sight-----------

#-----------Limit Switch-----------
LS_PIN = 26
GPIO.setup(LS_PIN, GPIO.IN)
#-----------Ultrasonic Sensor-----------
usTrig_PIN = 25
usEcho_PIN = 16
GPIO.setup(usTrig_PIN, GPIO.IN)
GPIO.setup(usEcho_PIN, GPIO.IN)

print("End Setup")
