from machine import ADC
from utime import sleep
pot = ADC(0)

while True:
    print ( pot.read_u16()) #on lit en binaire en 16 bit donc max on a 65535
    sleep(1)
