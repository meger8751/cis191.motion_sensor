import RPi.GPIO as GPIO
import time
import os
import subprocess
from random import randint

pir_sensor = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pir_sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

current_state = 0
time_count = 0
motion_count = 0

fast_count = 2
medium_count = randint(1,5)
slow_count = randint(1,5)

p = subprocess.Popen("exec timeout 58 mpg321 medium/medium" + str(medium_count)  + ".mp3 &", shell=True)

medium_count += 1


try:

    while True:
	if time_count == 30 :
	    print("30")
            if motion_count > 24 :
		p = subprocess.Popen("exec timeout 58 mpg321 fast/fast" + str(fast_count)  + ".mp3 &", shell = True)
		fast_count = fast_count % 5 + 1

	    elif motion_count < 20 :
		p = subprocess.Popen("exec timeout 58 mpg321 slow/slow" + str(slow_count) + ".mp3 &", shell = True)
              	slow_count = slow_count % 5 + 1

            else :       
		p = subprocess.Popen("exec timeout 58 mpg321 medium/medium" + str(medium_count)  + ".mp3 &", shell = True)
            
	        
	    time_count = 0
            motion_count = 0

        time.sleep(2)
        time_count += 1

	current_state = GPIO.input(pir_sensor)
        if current_state == 1:
            print('motion detected')
            motion_count += 1
	else:
            print('no motion detected')
    
			
except KeyboardInterrupt:
	pass
finally:
	GPIO.cleanup()
