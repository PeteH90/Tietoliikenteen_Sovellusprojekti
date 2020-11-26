import paho.mqtt.client as mqtt

broker_address="mqtt.eclipse.org"
client = mqtt.Client("P1")
client.connect(broker_address)
client.publish("testi","juh")
