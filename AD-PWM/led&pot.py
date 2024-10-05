from machine import ADC,Pin
from time import sleep

led = Pin(16,Pin.OUT)
pot = ADC(0)

while True:
    print (pot.read_u16())
    if pot.read_u16() > 30000:
        led.value(1)
        sleep(1)
    else:
        led.value(0)
        sleep(1)