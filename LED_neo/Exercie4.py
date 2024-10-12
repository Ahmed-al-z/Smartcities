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
orange = (255, 69, 0)       # Orange vif
pink = (255, 105, 180)      # Rose vif
lime = (50, 205, 50)        # Vert lime
turquoise = (64, 224, 208)  # Turquoise
indigo = (75, 0, 130)       # Indigo
violet = (238, 130, 238)    # Violet
gold = (255, 215, 0)        # Or
magenta = (255, 0, 255)     # Magenta
silver = (192, 192, 192)    # Argent
brown = (139, 69, 19)       # Brun
navy = (0, 0, 128)          # Bleu marine
teal = (0, 128, 128)        # Sarcelle (bleu-vert)
olive = (128, 128, 0)       # Olive
maroon = (128, 0, 0)        # Marron
light_blue = (173, 216, 230)  # Bleu clair
dark_blue = (0, 0, 139)       # Bleu foncé
light_green = (144, 238, 144) # Vert clair
dark_green = (0, 100, 0)      # Vert foncé
light_pink = (255, 182, 193)  # Rose clair
dark_red = (139, 0, 0)        # Rouge foncé
peach = (255, 218, 185)       # Pêche
salmon = (250, 128, 114)      # Saumon
khaki = (240, 230, 140)       # Kaki
coral = (255, 127, 80)        # Corail
orchid = (218, 112, 214)      # Orchidée
plum = (221, 160, 221)        # Prune
sky_blue = (135, 206, 235)    # Bleu ciel
mint = (189, 252, 201)        # Menthe
lavender = (230, 230, 250)    # Lavande
goldenrod = (218, 165, 32)    # Jaune doré
hot_pink = (255, 105, 180)    # Rose vif
crimson = (220, 20, 60)       # Carmin



colors= colors = (
    orange,      # Orange vif
    pink,        # Rose vif
    lime,        # Vert lime
    turquoise,   # Turquoise
    indigo,      # Indigo
    violet,      # Violet
    gold,        # Or
    magenta,     # Magenta
    silver,      # Argent
    brown,       # Brun
    navy,        # Bleu marine
    teal,        # Sarcelle (bleu-vert)
    olive,       # Olive
    maroon,      # Marron
    light_blue,  # Bleu clair
    dark_blue,   # Bleu foncé
    light_green, # Vert clair
    dark_green,  # Vert foncé
    light_pink,  # Rose clair
    dark_red,    # Rouge foncé
    peach,       # Pêche
    salmon,      # Saumon
    khaki,       # Kaki
    coral,       # Corail
    orchid,      # Orchidée
    plum,        # Prune
    sky_blue,    # Bleu ciel
    mint,        # Menthe
    lavender,    # Lavande
    goldenrod,   # Jaune doré
    hot_pink,    # Rose vif
    crimson      # Carmin
)



'''
on va mettre une condition qui dit: si le son depasse on change de couleur
pour ca on aura une variable pour le seuill une pour le debounce et une qui servira
a mettre a jour le temps.
et on va utiliser la fonction utime_ticks_ms qui sert a compter le temps depuis
la mise sous tension du RPI.
'''

seuil= 12000 # entre 8K-10K en silence 12K pour claquement de doight
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
