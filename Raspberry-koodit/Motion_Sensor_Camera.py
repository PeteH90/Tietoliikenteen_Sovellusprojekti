import RPi.GPIO as GPIO
from datetime import datetime
import time
from picamera import PiCamera

GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
message = 'start'
counter = 0
log_f = open('/home/pi/log.txt', 'w')
log_f.close()

camera = PiCamera()
pic_name = datetime.now()

camera.start_preview()
time.sleep(2)

while True:
    i=GPIO.input(11)
    if i==0:                 #When output from motion sensor is LOW
        if counter > 0:
            end = str(datetime.now())
            log_f = open('/home/pi/log.txt', 'a')
            message = message + '; end at ' + end + '\n'
            print(message)
            log_f.write(message)
            log_f.close()
            final = '/home/pi/' + str(pic_name) + ".jpg"
            camera.capture(final)
        counter = 0
        print("No intruders",i)
        time.sleep(0.1)
        
    elif i==1:               #When output from motion sensor is HIGH
        if counter == 0:
            current = str(datetime.now())
            message = 'Human detected:' + 'start at ' + current
        counter = counter + 1
        print("Intruder detected",i)
        time.sleep(0.1)
        
camera.stop_preview()