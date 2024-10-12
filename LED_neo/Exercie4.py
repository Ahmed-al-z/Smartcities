'''
-je dois lire les datas sonores dans une boucle.                         ok
-je dois analyer le son pour detecter les battements via un algo.       
-changer la couleur de la LED aleatoirement a chaque battement.         

'''
import machine
from ws2812 import WS2812
from machine import Pin,ADC
import utime
from utime import sleep
import random

led = WS2812(18,1) # (pin,count)
ss = ADC(1) #sound sensor

#black = (0,0,0)
red = (255,0,0)
yellow = (255,150,0)
green = (0,255,0)
cyan = (0,255,255)
blue = (0,0,255)
purple = (180,0,255)
white = (255,255,255)

colors=(red,yellow,green,cyan,blue,purple,white)


'''
on va mettre une condition qui dit: si le son depasse on change de couleur
pour ca on aura une variable pour le seuill une pour le debounce et une qui servira
a mettre a jour le temps.
et on va utiliser la fonction utime_ticks_ms qui sert a compter le temps depuis
la mise sous tension du RPI.
'''

seuil= 15000 # entre 8K-10K en silence 12K pour claquement de doight
previous = 0
debounce = 300

'''pour regler le probleme du capteur analogique je vais faire la moyenne 
des data audio'''
audio_val= []
audio_size = 10

def moyenne_audio (valeur):
    return sum(valeur) / len(valeur) # len : longeur



while True:
    audio = ss.read_u16() #for the rgb range
    audio_val.append(audio)
    if len(audio_val) > audio_size:
        audio_val.pop(0) # on retire la plus ancienne valeur enregister
    
    audio_final= moyenne_audio(audio_val)
    print(audio_final)

    if audio_final > seuil and (utime.ticks_ms() - previous )> debounce :
        
        rancol = random.choice(colors)
        led.pixels_fill(rancol)
        led.pixels_show()
        
        previous = utime.ticks_ms()
