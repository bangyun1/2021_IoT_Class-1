import RPi.GPIO as GPIO
import time

SWITCH_PIN = 12
SWITCH_PIN = 13
SWITCH_PIN = 14
SWITCH_PIN = 15
SWITCH_PIN = 16
SWITCH_PIN = 17
SWITCH_PIN = 18
SWITCH_PIN = 19
SWITCH_PIN = 20
SWITCH_PIN = 21
SWITCH_PIN = 22
SWITCH_PIN = 23
SWITCH_PIN = 24


GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PIN,GPIO.OUT)
#내부 풀다운저항(안눌렀을떄 0, 눌렀을때 :1)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# 주파수 설정 (262Hz)
pwm = GPIO.PWM(BUZZER_PIN, 262)
pwm.start(10) # duty cycle (0 ~10)

melody =[]

try:
    for i in melody:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)

    while True:
        val = GPIO.input(SWITCH_PIN)
        print(val)
        GPIO.output(LED_PIN, val) #GPIO.HIGH(1), GPIO.LOW(0)

finally:
    GPIO.cleanup()
    print('cleanup and exit')

    pwm.stop()
    GPIO.cleanup()
