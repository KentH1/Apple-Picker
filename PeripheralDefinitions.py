#Peripheral Definitions
print("Start Setup")
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM) #Sets reference to pins to be their GPIO __ number
#-----------Servos-----------
servoA1_PIN = 5
servoA2_PIN = 6
servoA3_PIN = 12
wrist_PIN = 23
grip_PIN = 24


GPIO.setup(servoA1_PIN, GPIO.OUT)
GPIO.setup(servoA2_PIN, GPIO.OUT)
GPIO.setup(servoA3_PIN, GPIO.OUT)
GPIO.setup(wrist_PIN, GPIO.OUT)
GPIO.setup(grip_PIN, GPIO.OUT)

pwm1 = GPIO.PWM(servoA1_PIN, 50) # GPIO 17 for PWM with 50Hz
pwm2 = GPIO.PWM(servoA2_PIN, 50) # GPIO 17 for PWM with 50Hz
pwm3 = GPIO.PWM(servoA3_PIN, 50) # GPIO 17 for PWM with 50Hz
pwm4 = GPIO.PWM(wrist_PIN, 50) # GPIO 17 for PWM with 50Hz
pwm5 = GPIO.PWM(grip_PIN, 50) # GPIO 17 for PWM with 50Hz

#-----------Stepper-----------
stepperPINS = [4,17,27,22] #[2B,2A,1A,1B]
for pin in stepperPINS:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)

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
