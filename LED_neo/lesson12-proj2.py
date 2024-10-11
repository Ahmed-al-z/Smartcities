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
    print(light,noise)

    if light < 80:
        led.pixels_fill((255,255,255))
        led.pixels_show()
        sleep(0.1)
    else:
        if noise > 50:
            led.pixels_fill((255,0,0))
            led.pixels_show()
            sleep(1)
        else:
            led.pixels_fill((0,255,0))
            led.pixels_show()
            sleep(1)
