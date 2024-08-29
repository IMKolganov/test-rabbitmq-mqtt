import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print(f"Unexpected disconnection. Return code: {rc}")
    else:
        print("Disconnected successfully")

client = mqtt.Client(client_id="my_mqtt_client_id")
client.on_connect = on_connect
client.on_disconnect = on_disconnect

broker_address = "localhost"  # Замените на адрес вашего брокера, если это необходимо
port = 1883  # Порт MQTT брокера

try:
    client.connect(broker_address, port, keepalive=60)  # Установите keepalive по необходимости
    client.loop_start()  # Запускает цикл обработки сетевых сообщений
except Exception as e:
    print(f"Failed to connect: {e}")

# Позволяет клиенту работать в фоновом режиме
import time
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Interrupted")
    client.loop_stop()
    client.disconnect()
