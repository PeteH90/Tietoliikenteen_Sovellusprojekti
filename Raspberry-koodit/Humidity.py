#!/usr/bin/python
import sys
import Adafruit_DHT
import paho.mqtt.client as mqtt
 
humidity, temperature = Adafruit_DHT.read_retry(11, 4)
#print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
temperature = "0"+str(temperature)
humidity = "1"+str(humidity)
broker_address="mqtt.eclipse.org"
client = mqtt.Client("P1")
client.connect(broker_address)
client.publish("kosteus1",humidity)
client.publish("lampotila1",temperature)