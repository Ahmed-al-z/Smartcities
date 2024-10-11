from machine import Pin
import machine
bp= machine.Pin(16,machine.Pin.IN)
fan = machine.Pin(18,machine.Pin.OUT)

while True:
    val = bp.value()
    if val ==1:
        fan.value(1)
    else:
        fan.value(0)