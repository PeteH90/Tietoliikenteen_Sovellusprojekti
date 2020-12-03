#!/usr/bin/python
import sys
import Adafruit_DHT
import paho.mqtt.client as mqtt
 
humidity, temperature = Adafruit_DHT.read_retry(11, 4)
print(temperature,humidity)
#print('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))
temperature = str(temperature)
humidity = str(humidity)
broker_address="mqtt.eclipse.org"
client = mqtt.Client("P1")
client.connect(broker_address)
client.publish("paavo_cabin_humidity_inside","2"+humidity)
client.publish("paavo_cabin_temperature_inside","0"+temperature)
