import RPi.GPIO as GPIO
import time

SERVO_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

servo = GPIO.PWM(SERVO_PIN, 50)
servo.start(0)

def open_lid():
    servo.ChangeDutyCycle(7)
    time.sleep(1)

def close_lid():
    servo.ChangeDutyCycle(2)
    time.sleep(1)