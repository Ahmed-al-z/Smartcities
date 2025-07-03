import network
import time
from machine import Pin, deepsleep
from umqtt.simple import MQTTClient
import camera

# Configurations des broches
led_ir = Pin(4, Pin.OUT)
pir_sensor = Pin(12, Pin.IN)

# Config Wi-Fi et MQTT
ssid = "ALZ-Home"
password = "jrmksp5phz3rze47"
mqtt_server = "192.168.129.19"
mqtt_topic = "camera/picture"
ack_topic = "camera/ack"  # Nouveau topic pour l'ACK

# Variables globales
ACK_RECEIVED = False
MAX_RETRIES = 3  # Nombre maximal de tentatives d'envoi
TIMEOUT = 5      # Temps d'attente pour l'ACK (en secondes)

def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    print("Module WiFi activé")
    
    wlan.connect(ssid, password)
    
    timeout = 20
    while not wlan.isconnected() and timeout > 0:
        print("Connexion en cours...")
        time.sleep(1)
        timeout -= 1
    if wlan.isconnected():
        print('Connecté au WiFi:', wlan.ifconfig())
    else:
        raise OSError("Connexion WiFi impossible.")

def init_camera():
    try:
        camera.init(0, format=camera.JPEG)
        camera.framesize(camera.FRAME_VGA)
        camera.quality(10)
        print("Caméra initialisée.")
    except Exception as e:
        print("Erreur d'initialisation de la caméra :", e)
        raise

def take_photo():
    try:
        img = camera.capture()
        return img
    except Exception as e:
        print("Erreur lors de la capture :", e)
        return None

def on_message(topic, msg):
    global ACK_RECEIVED
    if topic == ack_topic.encode() and msg == b"ACK":
        ACK_RECEIVED = True
        print("ACK reçu du Raspberry Pi.")

def send_photo(client, img):
    global ACK_RECEIVED
    retries = 0
    
    while retries < MAX_RETRIES:
        try:
            print(f"Tentative d'envoi {retries + 1}/{MAX_RETRIES}")
            client.publish(mqtt_topic, img)
            
            # Attendre l'ACK
            start_time = time.time()
            ACK_RECEIVED = False
            
            while not ACK_RECEIVED and (time.time() - start_time) < TIMEOUT:
                client.check_msg()  # Vérifier les messages entrants
                time.sleep(0.1)
            
            if ACK_RECEIVED:
                print("Photo envoyée avec succès.")
                return True
            else:
                print("Timeout, aucun ACK reçu.")
                retries += 1
                
        except Exception as e:
            print(f"Erreur lors de l'envoi : {e}")
            retries += 1
    
    print("Échec après plusieurs tentatives.")
    return False

# Connexion WiFi
connect_wifi(ssid, password)

# Configuration MQTT
client = MQTTClient("ESP32CAM", mqtt_server)
client.set_callback(on_message)
client.connect()
client.subscribe(ack_topic)
print("Connecté au serveur MQTT.")

# Initialisation caméra
init_camera()

# Boucle principale
while True:
    if pir_sensor.value() == 0:  # Détection mouvement
        print("Mouvement détecté !")
        led_ir.on()
        img = take_photo()
        if img:
            send_photo(client, img)
        led_ir.off()
        time.sleep(1)
    else:
        print("En attente de mouvement...")
        time.sleep(1)
