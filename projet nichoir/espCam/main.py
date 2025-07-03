import network
import time
from machine import Pin, deepsleep
from umqtt.simple import MQTTClient
import camera

def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF) #type client
    wlan.active(True)
    print("module wifi activé")
    
    wlan.connect(ssid, password)
    
    timeout = 20  # Timeout de 20 secondes
    while not wlan.isconnected() and timeout > 0:
        print("Connexion en cours...")
        time.sleep(1)
        timeout -= 1
    if wlan.isconnected():
        print('Connecté au WiFi:', wlan.ifconfig())
    else:
        raise OSError("Connexion WiFi impossible. Vérifiez le SSID/mot de passe ou la portée.")

def init_camera():
    try:
        camera.init(0, format=camera.JPEG)
        camera.framesize(camera.FRAME_VGA)  # Résolution moyenne
        camera.quality(10)  # Haute qualité
        camera.brightness(1)  # Augmente légèrement la luminosité
        camera.contrast(0)  # Aucun ajustement du contraste
        camera.saturation(0)  # Saturation normale
        print("Caméra initialisée avec paramètres personnalisés.")
    except Exception as e:
        print("Erreur d'initialisation de la caméra :", e)
        raise

def take_photo():
    try:
        img = camera.capture()
        return img
    except Exception as e:
        print("Erreur lors de la capture de la photo :", e)
        return None

def send_photo(client, topic, img):
    try:
        if img:
            client.publish(topic, img)
            print("Photo envoyée avec succès.")
        else:
            print("Aucune photo à envoyer.")
    except Exception as e:
        print("Erreur lors de l'envoi de la photo :", e)

# Configurations des broches
led_ir = Pin(4, Pin.OUT)
pir_sensor = Pin(12, Pin.IN)

# Informations Wi-Fi et MQTT
'''
ssid = "WiFi-Home-2C40"
password = "wp4r2drjrknne"
'''
'''ssid = "iPhone de Ahmed"
password = "ahmed4621"
'''

ssid = "ALZ-Home"
password = "jrmksp5phz3rze47"

mqtt_server = "192.168.129.19"
mqtt_topic = "camera/picture"

# Connexion au WiFi (fait une seule fois)
connect_wifi(ssid, password)

# Connexion au serveur MQTT (fait une seule fois)
try:
    client = MQTTClient("ESP32CAM", mqtt_server)
    client.connect()
    print("Connecté au serveur MQTT.")
except Exception as e:
    print("Erreur lors de la connexion au serveur MQTT :", e)
    raise

# Initialisation de la caméra (fait une seule fois)
init_camera()

# Boucle principale (vérifie uniquement le mouvement)
while True:
    if pir_sensor.value() == 0:  # Mouvement détecté
        print("Mouvement détecté")
        led_ir.on()
        img = take_photo()
        send_photo(client, mqtt_topic, img)
        led_ir.off()
        time.sleep(1)  # Pause après chaque photo
    else:
        print("Aucun mouvement détecté.")
        time.sleep(1)  # Pause avant la prochaine vérification

