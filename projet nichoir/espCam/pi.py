import paho.mqtt.client as mqtt
import os
from datetime import datetime

# Paramètres MQTT
BROKER = "localhost"
TOPIC = "camera/picture"
ACK_TOPIC = "camera/ack"  # Topic pour l'ACK
SAVE_DIR = "/home/alz/Desktop/pi_code/"

os.makedirs(SAVE_DIR, exist_ok=True)

def on_message(client, userdata, msg):
    print("Image reçue. Sauvegarde...")
    
    # Générer un nom de fichier unique
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(SAVE_DIR, f"image_{timestamp}.jpg")
    
    # Sauvegarder l'image
    with open(file_path, "wb") as f:
        f.write(msg.payload)
    
    print(f"Image sauvegardée : {file_path}")
    
    # Envoyer un ACK
    client.publish(ACK_TOPIC, "ACK")
    print("ACK envoyé.")

def main():
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(BROKER, 1883)
    client.subscribe(TOPIC)
    
    print("En attente d'images...")
    client.loop_forever()

if __name__ == "__main__":
    main()