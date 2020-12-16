import paho.mqtt.client as mqtt
import time
import ssl

viesti = ''

client = mqtt.Client("P1")
MQTT_Broker = "test.mosquitto.org"
MQTT_Port = 1883
Keep_Alive_Interval = 60

def on_connect(client, userdata, flags, rc):
  client.subscribe("paavo_cabin_motion_sensor", 0)
  
def on_message(client, obj, message):
    viesti = str(message.payload.decode("utf-8"))
    print viesti
    if viesti == 'on':
        file = open('/home/pi/koodit/PirSensor.txt', 'w')
        file.write('1')
        file.close()
    elif viesti == 'off':
        file = open('/home/pi/koodit/PirSensor.txt', 'w')
        file.write('0')
        file.close()
        
def on_subscribe(mosq, obj, mid, granted_qos):
  pass

client.on_connect = on_connect
client.on_message=on_message
client.on_subscribe = on_subscribe

client.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))
client.loop_forever()