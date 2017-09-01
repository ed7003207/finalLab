import RPi.GPIO as GPIO
import time

BtnPin = 15
aPin = 18
bPin = 22
cPin = 33
dPin = 11
ePin = 23
fPin = 32
gPin = 16

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(aPin, GPIO.OUT)
    GPIO.setup(bPin, GPIO.OUT)
    GPIO.setup(cPin, GPIO.OUT)
    GPIO.setup(dPin, GPIO.OUT)
    GPIO.setup(ePin, GPIO.OUT)
    GPIO.setup(fPin, GPIO.OUT)
    GPIO.setup(gPin, GPIO.OUT)
    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.output(aPin, GPIO.LOW)
    GPIO.output(bPin, GPIO.LOW)
    GPIO.output(cPin, GPIO.LOW)
    GPIO.output(dPin, GPIO.LOW)
    GPIO.output(ePin, GPIO.LOW)
    GPIO.output(fPin, GPIO.LOW)
    GPIO.output(gPin, GPIO.LOW)
def off():    
        GPIO.output(aPin, GPIO.HIGH)
        GPIO.output(bPin, GPIO.HIGH)
        GPIO.output(cPin, GPIO.HIGH)
        GPIO.output(dPin, GPIO.HIGH)
        GPIO.output(ePin, GPIO.HIGH)
        GPIO.output(fPin, GPIO.HIGH)
        #GPIO.output(gPin, GPIO.LOW)

def zero():
        GPIO.output(aPin, GPIO.HIGH)
        GPIO.output(bPin, GPIO.HIGH)
        GPIO.output(cPin, GPIO.HIGH)
        GPIO.output(dPin, GPIO.HIGH)
        GPIO.output(ePin, GPIO.HIGH)
        GPIO.output(fPin, GPIO.HIGH)
        #GPIO.output(gPin, GPIO.LOW)
def one():
            GPIO.output(aPin, GPIO.LOW)
            GPIO.output(bPin, GPIO.HIGH)
            GPIO.output(cPin, GPIO.HIGH)
            GPIO.output(dPin, GPIO.LOW)
            GPIO.output(ePin, GPIO.LOW)
            GPIO.output(fPin, GPIO.LOW)
            GPIO.output(gPin, GPIO.LOW) 
        
def counter0():
    while True:
        button = GPIO.input(BtnPin)
        if button == 0:
            print("0")
            GPIO.output(aPin, GPIO.HIGH)
            GPIO.output(bPin, GPIO.HIGH)
            GPIO.output(cPin, GPIO.HIGH)
            GPIO.output(dPin, GPIO.HIGH)
            GPIO.output(ePin, GPIO.HIGH)
            GPIO.output(fPin, GPIO.HIGH)
            GPIO.output(gPin, GPIO.LOW)

def counter1():
    while True:
        button = GPIO.input(BtnPin)
        if counter0() is True and button == 0:
            print("1")
            GPIO.output(aPin, GPIO.LOW)
            GPIO.output(bPin, GPIO.HIGH)
            GPIO.output(cPin, GPIO.HIGH)
            GPIO.output(dPin, GPIO.LOW)
            GPIO.output(ePin, GPIO.LOW)
            GPIO.output(fPin, GPIO.LOW)
            GPIO.output(gPin, GPIO.LOW)            

def destroy():
        GPIO.output(aPin, GPIO.LOW)
        GPIO.output(bPin, GPIO.LOW)
        GPIO.output(cPin, GPIO.LOW)
        GPIO.output(dPin, GPIO.LOW)
        GPIO.output(ePin, GPIO.LOW)
        GPIO.output(fPin, GPIO.LOW)
        GPIO.output(gPin, GPIO.LOW)          # led off
        GPIO.cleanup()                          # Release resource

if __name__ == '__main__':                      # Program starts here
        setup()
       

        try:
                counter0()
                counter1()
        except KeyboardInterrupt:               # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
                destroy()
        
    
    


    
