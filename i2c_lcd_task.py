from lcd import drivers
import time
import datetime
import Adafruit_DHT
display = drivers.Lcd()
now = datetime.datetime.now()
sensor = Adafruit_DHT.DHT11
pin = 5

try:
    print('Writing to Display')
    while True:
        display.lcd_display_string(now.strftime("%x%X"),1)
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        if humidity is not None and temperature is not None:
            display.lcd_display_string(f"Temperature={temperature:.1f}C, Humidity:{humidity:.1f}%",2)
        else:
            display.lcd_display_string('Read error')
        time.sleep(1)

    
finally:
    print("cleaning up")
    display.lcd_clear()