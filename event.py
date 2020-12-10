import paho.mqtt.client as mqtt
import ssl
import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='testi1', password='!Anturidata123', database='cabin_monitor')
cursor = mariadb_connection.cursor()

msg_dict = {}

Q1 = "select id_temperature_inside from temperature_inside order by id_temperature_inside desc LIMIT 1"
Q2 = "select id_temperature_outside from temperature_outside order by id_temperature_outside desc LIMIT 1"
Q3 = "select id_humidity_inside from humidity_inside order by id_humidity_inside desc LIMIT 1"
Q4 = "select id_humidity_outside from humidity_outside order by id_humidity_outside desc LIMIT 1"
Q5 = "select id_air_pressure from air_pressure order by id_air_pressure desc LIMIT 1"
Q6 = "

cursor.execute(Q1)
Q1 = cursor.fetchall()
for row in Q1:
  Q01 = row[0]

cursor.execute(Q2)
Q2 = cursor.fetchall()
for row in Q2:
  Q02 = row[0]

cursor.execute(Q3)
Q3 = cursor.fetchall()
for row in Q3:
  Q03 = row[0]

cursor.execute(Q4)
Q4 = cursor.fetchall()
for row in Q4:
  Q04 = row[0]

cursor.execute(Q5)
Q5 = cursor.fetchall()
for row in Q5:
  Q05 = row[0]

sql = "INSERT INTO _events VALUES (NULL, '%s', '%s', '%s', '%s', NULL, '%s', 1, NOW())" % (Q03, Q04, Q02, Q01, Q05)

try:
      cursor.execute(sql, msg_dict.values())
except mariadb.Error as error:
      print("Error: {}".format(error))
mariadb_connection.commit()

mariadb_connection.close()
