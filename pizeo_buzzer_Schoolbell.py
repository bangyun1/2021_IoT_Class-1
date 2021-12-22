#도레미파솔라시도 출력하기
import RPi.GPIO as GPIO
import time

BUZZER_PIN = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# 주파수 설정 (262Hz)
pwm = GPIO.PWM(BUZZER_PIN, 262)
pwm.start(10) # duty cycle (0 ~10)

#도레미파솔라시도
melody = [349,392,440,349,523,440,392,523,392,349,294,440,349,
330,349,330,294,330,349,392,262,349,392,440,466,466,440,392,349,
392,349,392,440,349,523,440,392,523,392,349,294,294,330,349,262,262,
294,330,349,392,262,349,
392,440,466,466,440,392,349,349]

try:
    for i in melody:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)


finally:
    pwm.stop()
    GPIO.cleanup()


