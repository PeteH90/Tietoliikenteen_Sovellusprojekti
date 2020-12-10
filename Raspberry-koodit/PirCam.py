import RPi.GPIO as GPIO
from datetime import datetime
import time
from picamera import PiCamera
import paho.mqtt.client as mqtt
import cv2 
import imutils 

hog = cv2.HOGDescriptor() 
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
message = 'start'
counter = 0
log_f = open('/home/pi/log.txt', 'w')
log_f.close()

camera = PiCamera()
pic_name = 0


viesti1 = "'human detected'"
viesti2 = "'movement detected'"
#camera.start_preview()
time.sleep(60)

while True:
    i=GPIO.input(11)
    regions = 0
    if i==0: #When output from motion sensor is LOW
        if counter > 50:
            end = str(datetime.now())
            log_f = open('/home/pi/log.txt', 'a')
            message = message + '; end at ' + end + '\n'
            print(message)
            log_f.write(message)
            log_f.close()
            final = '/home/pi/kuvat/kuva' + str(pic_name) + ".jpg"
            pic_name = pic_name + 1
            camera.capture(final)
            image = cv2.imread('/home/pi/kuvat/kuvaa3.jpg')
            image = imutils.resize(image, 
                       width=min(400, image.shape[1]))
            (regions, _) = hog.detectMultiScale(image,  
                                    winStride=(4, 4), 
                                    padding=(4, 4), 
                                    scale=1.05)
            pituus = str(len(regions))
            if len(regions) > 0:
                #broker_address="broker.hivemq.com"
                #client = mqtt.Client("P1")
                #client.connect(broker_address)
                #client.publish("paavo_cabin_message","5"+pituus+viesti1)
                print("5"+pituus+viesti1)
            else:
                #broker_address="broker.hivemq.com"
                #client = mqtt.Client("P1")
                #client.connect(broker_address)
                #client.publish("paavo_cabin_message","5"+viesti2)
                print("!")
        counter = 0
        cv2.destroyAllWindows() 
        print("No intruders",i)
        time.sleep(0.1)
        
    elif i==1:         #When output from motion sensor is HIGH
        if counter == 0:
            current = str(datetime.now())
            message = 'Human detected:' + 'start at ' + current
        counter = counter + 1
        print("Intruder detected",i)
        time.sleep(0.1)
        
#camera.stop_preview()