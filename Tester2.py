import time
import xbox
import RPi.GPIO as GPIO

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

def right():
    wheelForwardL()
    wheelReverseR()

def left():
    wheelForwardR()
    wheelReverseL()
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




def wheelOffL():
    GPIO.output(PWMB,GPIO.LOW)
    GPIO.output(PWMA, GPIO.LOW)
def wheelOffR():
    GPIO.output(PWMC,GPIO.LOW)
    GPIO.output(PWMD, GPIO.LOW)
    
movement =[]
direction = []

def joyLeftYF():
    if joy.leftY() > 0:
        if joy.leftY() > 0 and joy.rightY > 0:
            joyForward()
        if joy.leftY() > 0 and joy.rightY < 0:
            joyRight()
        timeStart = time.time()
        while joy.leftY()> 0:
            if joy.rightY > 0:
                timeEnd = time.time()
                total = timeEnd - timeStart
                movement.append(total)
                direction.append("wheelReverseL()")
                joyForward()
            if joy.rightY < 0:
                timeEnd = time.time()
                total = timeEnd - timeStart
                movement.append(total)
                direction.append("wheelReverseL()")
                joyRight()
            wheelForwardL()
    if joy.leftY() == 0:
        timeEnd = time.time()
        total = timeEnd - timeStart
        movement.append(total)
        direction.append("wheelReverseL()")

        start()
        
def joyLeftYR():
    if joy.leftY() < 0:
        if joy.leftY() < 0 and joy.rightY() < 0:
            joyReverse()
        if joy.leftY() < 0 and joy.rightY() > 0:
            joyLeft()
        timeStart = time.time()
        while joy.leftY() < 0:
            wheelReverseL()
    if joy.leftY() == 0:
        timeEnd = time.time()
        total = timeEnd - timeStart
        movement.append(total)
        direction.append("wheelForwardL()")
        start()

def joyRightYF():
    if joy.rightY() > 0:
        if joy.rightY() > 0 and joy.leftY > 0:
            joyForward()
        if joy.rightY() > 0 and joy.leftY < 0:
            joyLeft()
        timeStart = time.time()
        while joy.rightY() > 0:
            wheelForwardR()
    if joy.rightY() == 0:
        timeEnd = time.time()
        total = timeEnd - timeStart
        movement.append(total)
        direction.append("wheelReverseR()")
        start()

def joyRightYR():
    if joy.rightY() < 0:
        if joy.rightY() < 0 and joy.leftY < 0:
            joyReverse()
        if joy.rightY() < 0 and joy.leftY > 0:
            joyRight()
        timeStart = time.time()
        while joy.rightY() < 0:
            wheelForwardR()
    if joy.rightY() == 0:
        timeEnd = time.time()
        total = timeEnd - timeStart
        movement.append(total)
        direction.append("wheelForwardR()")
        start()

def joyForward():
    if (joy.rightY() > 0) and (joy.leftY() > 0):
        if (joy.rightY() > 0) and (joy.leftY() < 0):
            joyLeft()
        if (joy.rightY() < 0) and (joy.leftY() > 0):
            joyRight()
        timeStart = time.time()
        while (joy.rightY() > 0) and (joy.leftY() > 0):
            allForward()
    if (joy.rightY() == 0) and (joy.leftY() == 0):
        timeEnd = time.time()
        total = timeEnd - timeStart
        movement.append(total)
        direction.append("allReverse()")
        start()

def joyReverse():
    if (joy.rightY() < 0) and (joy.leftY() < 0):
        if (joy.rightY() > 0) and (joy.leftY() < 0):
            joyLeft()
        if (joy.rightY() < 0) and (joy.leftY() > 0):
            joyRight()
        timeStart = time.time()
        while (joy.rightY() < 0) and (joy.leftY() < 0):
            allReverse()
    if (joy.rightY() == 0) and (joy.leftY() == 0):
        timeEnd = time.time()
        total = timeEnd - timeStart
        movement.append(total)
        direction.append("allForward()")
        start()

def joyRight():
    if (joy.rightY() < 0) and (joy.leftY() > 0):
        timeStart = time.time()
        while (joy.rightY() < 0) and (joy.leftY() > 0):
            right()
    if (joy.rightY() == 0) and (joy.leftY() == 0):
        timeEnd = time.time()
        total = timeEnd - timeStart
        movement.append(total)
        direction.append("left()")
        start()

def joyLeft():
    if (joy.rightY() > 0) and (joy.leftY() < 0):
        timeStart = time.time()
        while (joy.rightY() > 0) and (joy.leftY() < 0):
            left()
    if (joy.rightY() == 0) and (joy.leftY() == 0):
        timeEnd = time.time()
        total = timeEnd - timeStart
        movement.append(total)
        direction.append("right()")
        start()



        
def stopL():
    wheelOffL()
def stopR():
    wheelOffR()
def start(): 
    while not joy.Back():
        setup()
        print (movement)
        print(direction)
        if joy.leftY()>0:
            joyLeftYF()
        if joy.leftY() == 0:
            stopL()
        if joy.leftY() < 0:
            joyLeftYR()
        if joy.rightY() > 0:
            joyRightYF()
        if joy.rightY() < 0:
            joyRightYR()
        if joy.rightY() == 0:
            stopR()
        if (joy.rightY() > 0) and (joy.leftY() > 0):
            joyForward()
        if (joy.rightY() < 0) and (joy.leftY() < 0):
            joyReverse()
        if (joy.rightY() < 0) and (joy.leftY() > 0):
            joyRight()
        if (joy.rightY() > 0) and (joy.leftY() < 0):
            joyLeft()
start()
