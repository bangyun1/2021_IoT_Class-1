import RPi.GPIO as GPIO
import time
import threading

LED_PIN = 4
SWITCH_PIN = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN,GPIO.OUT)
#내부 풀다운저항(안눌렀을떄 0, 눌렀을때 :1)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_PIN, GPIO.IN)

try:
    while True:
        val = GPIO.input(SWITCH_PIN)
        print(val)
        time.sleep(5)
    
        while True:
            val = GPIO.input(SWITCH_PIN)
            print(val)
            GPIO.output(LED_PIN, val) #GPIO.HIGH(1), GPIO.LOW(0)
        
            if val:
                def printSetTheAlarm5minutes():
                    print("Counting seconds..")

                #threading을 정의한다. 5분마다 반복 수행함
                threading.Timer(3, printSetTheAlarm5minutes).start()
            
                def AlarmIsDone():
                    print("Counting is done")

finally: 
    GPIO.cleanup()
    print('cleanup and exit')