import machine
from machine import Pin
import utime

bp= machine.Pin(16,machine.Pin.IN)
fan = machine.Pin(18,machine.Pin.OUT)
val = 0

while True:
    val = bp.value()
    if val ==1:
        fan.toggle()
        utime.sleep_ms(100)