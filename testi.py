import paho.mqtt.client as mqtt
import ssl
import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='testi1', password='!Anturidata123', database='cabin_monitor')
cursor = mariadb_connection.cursor()

# MQTT Settings
MQTT_Broker = "mqtt.eclipse.org"
MQTT_Port = 1883
Keep_Alive_Interval = 60
MQTT_Topic = ["paavo_cabin_temperature_inside", "paavo_cabin_temperature_outside", "paavo_cabin_humidity_inside", "paavo_cabin_humidity_outside", "paavo_cabin_airpressure", "paavo_cabin_message"]

# Subscribe
def on_connect(client, userdata, flags, rc):
  mqttc.subscribe(MQTT_Topic[0], 0)
  mqttc.subscribe(MQTT_Topic[1], 0)
  mqttc.subscribe(MQTT_Topic[2], 0)
  mqttc.subscribe(MQTT_Topic[3], 0)
  mqttc.subscribe(MQTT_Topic[4], 0)
  mqttc.subscribe(MQTT_Topic[5], 0)


def on_message(mosq, obj, msg):
  # Prepare Data
  muuttuja = ""
  print(msg.payload)
  msg_clear = msg.payload.decode("utf-8") 
  msg_dict = {}
  print(msg_clear)
  leikkaus = msg_clear[:1]
  leikkaus2 = msg_clear[1:]

  if leikkaus == '0':
    muuttuja = "temperature_inside"
  elif leikkaus == '1':
    muuttuja = "temperature_outside"
  elif leikkaus == '2':
    muuttuja = "humidity_inside"
  elif leikkaus == '3':
    muuttuja = "humidity_outside"
  elif leikkaus == '4':
    muuttuja = "air_pressure"
  elif leikkaus == '5':
    muuttuja = "messages"

#  Prepare sql statement

  sql = "INSERT INTO %s VALUES (NULL, %s, NOW(), 1)" % (muuttuja, leikkaus2)

# Save Data into DB Table
  try:
      cursor.execute(sql, msg_dict.values())
  except mariadb.Error as error:
      print("Error: {}".format(error))
  mariadb_connection.commit()

def on_subscribe(mosq, obj, mid, granted_qos):
  pass

mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.on_subscribe = on_subscribe

# Connect
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))

# Continue the network loop & close db-connection
mqttc.loop_forever()
mariadb_connection.close()
