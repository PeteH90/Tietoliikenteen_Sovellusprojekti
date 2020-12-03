import bme280
import smbus2
from time import sleep
import paho.mqtt.client as mqtt

port = 1
address = 0x76 # Adafruit BME280 address. Other BME280s may be different
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus,address)

bme280_data = bme280.sample(bus,address)
humidity  = bme280_data.humidity
pressure  = bme280_data.pressure
ambient_temperature = bme280_data.temperature

ambient_temperature = round(ambient_temperature,1)
pressure = round(pressure,1)
pressure = str(pressure)
temperature = str(ambient_temperature)

broker_address="mqtt.eclipse.org"
client = mqtt.Client("P1")
client.connect(broker_address)
client.publish("paavo_cabin_temperature_outside","1"+temperature)
client.publish("paavo_cabin_airpressure","4"+pressure)