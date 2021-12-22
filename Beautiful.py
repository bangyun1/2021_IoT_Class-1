import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

led1 = 14
led2 = 15
led3 = 18
led4 = 17
led5 = 24
led6 = 25
led7 = 4
led8 = 3
buzzer = 23
do = 21
re = 2
mi = 16
fa = 26
sol = 19
ra = 13
si = 6
do2 = 5
scale = [261,294,329,349,392,440,493,523,1]
GPIO.setup(buzzer,GPIO.OUT)
#불확실 코드
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)
GPIO.setup(led5, GPIO.OUT)
GPIO.setup(led6, GPIO.OUT)
GPIO.setup(led7, GPIO.OUT)
GPIO.setup(led8, GPIO.OUT)
GPIO.setup(do, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(re, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(mi, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(fa, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(sol, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(ra, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(si, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(do2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#불확실 코드

p = GPIO.PWM(buzzer,600)

p.start(10)

try:
    while True: 
        if GPIO.input(do) == GPIO.HIGH :
            p.ChangeFrequency(scale[0])
            val = GPIO.input(do)
            print(val)
            GPIO.output(led1, val)

        elif GPIO.input(re) == GPIO.HIGH :
            p.ChangeFrequency(scale[1])
            val = GPIO.input(re)
            print(val)
            GPIO.output(led2, val)
            
        elif GPIO.input(mi) == GPIO.HIGH :
            p.ChangeFrequency(scale[2])
            val = GPIO.input(mi)
            print(val)
            GPIO.output(led3, val)

        elif GPIO.input(fa) == GPIO.HIGH :
            p.ChangeFrequency(scale[3])
            val = GPIO.input(fa)
            print(val)
            GPIO.output(led4, val)

        elif GPIO.input(sol) == GPIO.HIGH :
            p.ChangeFrequency(scale[4])
            val = GPIO.input(sol)
            print(val)
            GPIO.output(led5, val)

        elif GPIO.input(ra) == GPIO.HIGH :
            p.ChangeFrequency(scale[5])
            val = GPIO.input(ra)
            print(val)
            GPIO.output(led6, val)
        
        elif GPIO.input(si) == GPIO.HIGH :
            p.ChangeFrequency(scale[6])
            val = GPIO.input(si)
            print(val)
            GPIO.output(led7, val)

        elif GPIO.input(do2) == GPIO.HIGH :
            p.ChangeFrequency(scale[7])
            val = GPIO.input(do2)
            print(val)
            GPIO.output(led8, val)

        else :
            p.ChangeFrequency(scale[8])

        #불확실
    

finally:
    p.stop()
    GPIO.cleanup()