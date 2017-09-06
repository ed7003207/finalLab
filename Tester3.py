import xbox
import RPi.GPIO as GPIO
import time

def fmtFloat(n):
    return '{:6.3f}'.format(n)
    
joy = xbox.Joystick()
GPIO.setmode(GPIO.BOARD)
#Front Left
Motor1A = 11
Motor2A = 13
PWMA = 15
#Back Left
Motor1B = 33
Motor2B = 35
PWMB = 37
#Front Right
Motor1C = 16
Motor2C = 18
PWMC= 12
#Back Right
Motor1D = 36
Motor2D =38
PWMD = 40

Turret = 7

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
#Turret
    GPIO.setup(Turret, GPIO.OUT)

def turnTurret():
    GPIO.output(Turret, GPIO.HIGH)

def stopTurret():
    GPIO.output(Turret, GPIO.LOW)

def allForward():
    wheelForward_FrontL()
    wheelForward_BackL()
    
    wheelForward_FrontR()
    wheelForward_BackR()

def allReverse():
    wheelReverse_FrontL()
    wheelReverse_BackL()
    wheelReverse_FrontR()
    wheelReverse_BackR()

"""
Move Per Side
"""

def wheelForwardL():
    wheelForward_FrontL()
    wheelForward_BackL()

def wheelForwardR():
    wheelForward_FrontR()
    wheelForward_BackR()

def wheelReverseL():
    wheelReverse_FrontL()
    wheelReverse_BackL()

def wheelReverseR():
    wheelReverse_FrontR()
    wheelReverse_BackR()



"""
Forward Left Side
"""
def wheelForward_FrontL():
    #Front Left
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(PWMA,GPIO.HIGH)
def wheelForward_BackL():
    #Back Left
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(PWMB,GPIO.HIGH)
    print("Turning")
    
"""
Forward Right Side
"""
def wheelForward_FrontR():
    #Front Right
    GPIO.output(Motor1C,GPIO.LOW)
    GPIO.output(Motor2C,GPIO.HIGH)
    GPIO.output(PWMC,GPIO.HIGH)
def wheelForward_BackR():
    #Back Right
    GPIO.output(Motor1D,GPIO.LOW)
    GPIO.output(Motor2D,GPIO.HIGH)
    GPIO.output(PWMD,GPIO.HIGH)
"""
Reverse Left Side
"""
def wheelReverse_FrontL():
    #Front Left
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(PWMA,GPIO.HIGH)
def wheelReverse_BackL():
    #Back Left
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
    GPIO.output(PWMB,GPIO.HIGH)
"""
Reverse Right Side
"""
def wheelReverse_FrontR():
    GPIO.output(Motor1C,GPIO.HIGH)
    GPIO.output(Motor2C,GPIO.LOW)
    GPIO.output(PWMC,GPIO.HIGH)
def wheelReverse_BackR():
    GPIO.output(Motor1D,GPIO.HIGH)
    GPIO.output(Motor2D,GPIO.LOW)
    GPIO.output(PWMD,GPIO.HIGH)
    print("Turning")




def wheelOffL():
    GPIO.output(PWMB,GPIO.LOW)
    GPIO.output(PWMA, GPIO.LOW)
def wheelOffR():
    GPIO.output(PWMC,GPIO.LOW)
    GPIO.output(PWMD, GPIO.LOW)

def time():
    timeStart = time.time()

"""



"""
movementL = []
movementR = []
directionL = []
directionR = []
left = 0
right = 0
wheelFL = 0
wheelRL = 0
wheelFR = 0
wheelRR = 0
while not joy.Back():
    setup()

    if joy.leftY()>0:
        left = 1
        wheelFL = wheelFL + 1
        wheelForwardL()
    elif (joy.leftY()==0) and (left == 1):
        left = 0
        movementL.append(wheelFL)
        if joy.rightY() == 0:
            movementR.append(wheelRL)
            directionR.append("0")
        wheelFL = 0
        directionL.append("wheelForwardL")
        wheelOffL()
    if joy.leftY()<0:
        left = -1
        wheelRL = wheelRL + 1
        wheelReverseL()
    elif (joy.leftY()==0) and (left == -1):
        left = 0
        movementL.append(wheelRL)
        if joy.rightY() == 0:
            movementR.append(wheelRR)
            directionR.append("0")
        wheelRL = 0
        directionL.append("wheelReverseL")
        wheelOffL()


        
    #Right Analog Stick
    if joy.rightY()>0:
        right = 1
        wheelFR = wheelFR + 1
        wheelForwardR()
    elif (joy.rightY()==0) and (right == 1):
        right = 0
        movementR.append(wheelFR)
        if joy.leftY() == 0:
            movementL.append(wheelFL)
            directionL.append("0")
        wheelRL = 0
        directionR.append("wheelReverseR")
        wheelOffR()
    if joy.rightY()<0:
        right = -1
        wheelRR = wheelRR + 1
        wheelReverseR()
    elif (joy.rightY()==0) and (right == -1):
        right = 0
        movementR.append(wheelRR)
        if joy.leftY() == 0:
            movementL.append(wheelRL)
            directionL.append("0")
        wheelRR = 0
        directionR.append("wheelReverseR")
        wheelOffR()


    print (movementL)
    print (movementR)
    print(directionL)
    print(directionR)
