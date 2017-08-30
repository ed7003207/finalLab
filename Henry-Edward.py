import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
 
Motor1B = 33
Motor2B = 35
PWMB = 37
Motor1A = 11
Motor2A = 13
PWMA = 15

Motor1C = 16
Motor2C = 18
PWMC= 12
Motor1D = 36
Motor2D =38
PWMD = 40
def setup():
#Left Side
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor2B,GPIO.OUT)
    GPIO.setup(PWMB,GPIO.OUT)
    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor2A,GPIO.OUT)
    GPIO.setup(PWMA,GPIO.OUT)
# Right Side    
    GPIO.setup(Motor1C,GPIO.OUT)
    GPIO.setup(Motor2C,GPIO.OUT)
    GPIO.setup(PWMC,GPIO.OUT)
    GPIO.setup(Motor1D,GPIO.OUT)
    GPIO.setup(Motor2D,GPIO.OUT)
    GPIO.setup(PWMD,GPIO.OUT)
#Left Side    
def wheelOnL():
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(PWMB,GPIO.HIGH)
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(PWMA,GPIO.HIGH)
    print("Turning")

def wheelOnAltL():
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
    GPIO.output(PWMB,GPIO.HIGH)
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(PWMA,GPIO.HIGH)

#Right Side
def wheelAltR():
    GPIO.output(Motor1C,GPIO.HIGH)
    GPIO.output(Motor2C,GPIO.LOW)
    GPIO.output(PWMC,GPIO.HIGH)
    GPIO.output(Motor1D,GPIO.HIGH)
    GPIO.output(Motor2D,GPIO.LOW)
    GPIO.output(PWMD,GPIO.HIGH)
    print("Turning")
    
def wheelOnR():
    GPIO.output(Motor1C,GPIO.LOW)
    GPIO.output(Motor2C,GPIO.HIGH)
    GPIO.output(PWMC,GPIO.HIGH)
    GPIO.output(Motor1D,GPIO.LOW)
    GPIO.output(Motor2D,GPIO.HIGH)
    GPIO.output(PWMD,GPIO.HIGH)

def wheelOff():
    GPIO.output(PWMB,GPIO.LOW)
    GPIO.output(PWMA, GPIO.LOW)
    GPIO.output(PWMC,GPIO.LOW)
    GPIO.output(PWMD, GPIO.LOW)
if __name__ == "__main__":
    setup()

