import machine
from machine import I2C,Pin,ADC
from utime import sleep
from ws2812 import WS2812

led = WS2812(18,1)
ls=ADC(0)
ss=ADC(1)

while True:
    light= ls.read_u16()/256
    noise = ss.read_u16()/256
    print(light)
    
