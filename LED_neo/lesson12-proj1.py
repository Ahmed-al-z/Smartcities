from ws2812 import WS2812
import utime

black = (0,0,0)
red = (255,0,0)
yellow = (255,150,0)
green = (0,255,0)
cyan = (0,255,255)
blue = (0,0,255)
purple = (180,0,255)
white = (255,255,255)

colors=(black,red,yellow,green,cyan,blue,purple,white)

led = WS2812(18,1)

while True:
    print("fills")
    for color in colors:
        led.pixels_fill(color)
        led.pixels_show()
        utime.sleep(0.2)