import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
TOPIC = "smartdustbin/data"

client = mqtt.Client()

def send_data(payload):
    client.connect(BROKER, 1883, 60)
    client.publish(TOPIC, payload)
    client.disconnect()