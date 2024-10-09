import machine
import utime
from time import sleep
bp = machine.Pin(18,machine.Pin.IN)
led = machine.Pin(machine.Pin.OUT)

# donc je vais ajouter une variable pour l'etat du bp et une autre
#pour stocker l'etat precident

bp_etat = bp.value()
cycle = 0
PP_PREC = 0


while True:
    bp_etat = bp.value()

   
    
  
    led.value(1)
    utime.sleep (1)
    led.value(0)
        