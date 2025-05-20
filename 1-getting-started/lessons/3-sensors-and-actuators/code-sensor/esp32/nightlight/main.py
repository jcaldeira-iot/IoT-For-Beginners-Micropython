import time
from machine import ADC, Pin

light_sensor = ADC(5)

while True:
    light = light_sensor.read()
    print('Light level:', light)
    
    time.sleep(1)
