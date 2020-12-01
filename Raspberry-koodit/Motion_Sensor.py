import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
import Humidity_Temperature

broker_address="mqtt.eclipse.org"
GPIO.setmode(GPIO.BOARD) #Set GPIO to pin numbering
pir = 8 #Assign pin 8 to PIR
GPIO.setup(pir, GPIO.IN) #Setup GPIO pin PIR as input
time.sleep(2) #Give sensor time to startup

while True:
    if GPIO.input(pir) == True: #If PIR pin goes high, motion is detected
        client = mqtt.Client("P1")
        client.connect(broker_address)
        client.publish("MotionSensooriTesti","1")
        execfile('Humidity_Temperature.py')
        time.sleep(5)




