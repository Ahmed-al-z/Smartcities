# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
# Complete project details at https://RandomNerdTutorials.com/micropython-programming-with-esp32-and-esp8266/

import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

ssid = 'WiFi-Home-2C40'
password = 'wp4r2drjrknne'
mqtt_server = 'smarts'
mqtt_user = 'ahmed'
mqtt_pass = 'city'

#EXAMPLE IP ADDRESS
#mqtt_server = '192.168.1.144'
client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'notification'
topic_pub = b'hello'

last_message = 0
message_interval = 5
counter = 0

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid,password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())
