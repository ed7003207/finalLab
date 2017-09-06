import RPi.GPIO as GPIO
import time
import xbox

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

pwm = GPIO.PWM(7, 50)
#pwm.start(5)


joy = xbox.Joystick()

while not joy.Back():

    if joy.rightTrigger():
        pwm.start(10)
    if joy.leftTrigger():
        pwm.start(5)
    if joy.A():
        pwm.start(0)
        
