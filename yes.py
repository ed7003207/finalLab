import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO_Servo = 7

GPIO.setup(GPIO_Servo, GPIO.OUT)

pwm_frequency = 50

def set_duty_cycle(angle):
    pulse =  2*float(angle)/180.0 + 0.5
    duty = 0.1*pulse*pwm_frequency
    #duty = 2.5 + 0.12*float(angle) for frequency of 100
    return duty

pwm_servo = GPIO.PWM(GPIO_Servo, pwm_frequency)
pwm_servo.start(90)
