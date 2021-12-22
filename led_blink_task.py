import RPi.GPIO as GPIO
import time

RED = 22
YELLOW = 27
GREEN = 17
GPIO.setmode(GPIO.BCM)

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)

for i in range(10):
    print("led on green")
    time.sleep(1)
    GPIO.output(GREEN, GPIO.HIGH)
    print("led off green")
    time.sleep(1)
    GPIO.output(GREEN, GPIO.LOW)
    
    print("led on yellow")
    time.sleep(1)
    GPIO.output(YELLOW, GPIO.HIGH)
    print("led off yellow")
    time.sleep(1)
    GPIO.output(YELLOW, GPIO.LOW)
    
    print("led on red")
    time.sleep(1)
    GPIO.output(RED, GPIO.HIGH)
    print("led off red")
    time.sleep(1)
    GPIO.output(RED, GPIO.LOW)
    


GPIO.cleanup()