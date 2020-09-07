import PeripheralDefinitions
import analogSetup
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
#import SPI_Trial_Setup
#-----------Servo Setup-----------
class main_joint:
    def __init__(self,servoPin,freq):
        self.servoPin=servoPin
        self.pwm=0
    def servo_setup(self):
        GPIO.setup(self.servoPin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.servoPin, self.freq) # GPIO pin for PWM with 50Hz
        self.pwm.start(0)
    def move(self,angle):
        duty=self.angle/18+2
        self.pwm.ChangeDutyCycle(duty)

j1=main_joint(5,50)
j2=main_joint(6,50)
j3=main_joint(12,50)
j4=main_joint(23,50)
j5=main_joint(24,50)
j1.servo_setup()
j2.servo_setup()
j3.servo_setup()
j4.servo_setup()
j5.servo_setup()

#-----------Stepper Setup-----------
class slider:
    def __init__(self,stepperPINS):
        self.stepperPINS= stepperPINS
    def stepper_setup(self):
        GPIO.setup(self.stepperPINS, GPIO.OUT)
        GPIO.output(self.stepperPINS, 0)
    def move(self):
        GPIO.output(self.stepperPINS, 1)

#-----------X-----------
def main():
    print("Hello World")
#def home():

def stop():
    j1.pwm.stop()
    GPIO.cleanup()
    