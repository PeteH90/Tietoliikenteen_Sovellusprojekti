import paho.mqtt.client as mqtt
import time

viesti = ''

def on_message(client, userdata, message):
    time.sleep(1)
    viesti = str(message.payload.decode("utf-8"))
    return True

broker_address="broker.hivemq.com"
client = mqtt.Client("P1")
client.on_message=on_message
client.connect(broker_address)
client.loop_start()
client.subscribe("paavo_cabin_motion_sensor")
time.sleep(2)
client.disconnect()
client.loop_stop()