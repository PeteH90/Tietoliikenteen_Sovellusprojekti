'import paho.mqtt.client as mqtt
import ssl
import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='testi1', password='!Anturidata123', database='anturidata')
cursor = mariadb_connection.cursor()

# MQTT Settings
MQTT_Broker = "mqtt.eclipse.org"
MQTT_Port = 1883
Keep_Alive_Interval = 60
MQTT_Topic = ["kosteus1", "lampotila1", "ilmanpaine1"]

# Subscribe
def on_connect(client, userdata, flags, rc):
  mqttc.subscribe(MQTT_Topic[0], 0)
  mqttc.subscribe(MQTT_Topic[1], 0)


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
    muuttuja = "Lampotila"
  elif leikkaus == '1':
    muuttuja = "Kosteus"
  elif leikkaus == '2':
    muuttuja = "Ilmanpaine"
  print(muuttuja)
#  Prepare sql statement

  sql = "INSERT INTO %s VALUES (NULL, %s )" % (muuttuja, leikkaus2)

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
