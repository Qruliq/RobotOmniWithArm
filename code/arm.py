import RPi.GPIO as GPIO
import time
import Servo as servo
from evdev import InputDevice, categorize, ecodes

GPIO.setmode(GPIO.BOARD)

gamepad = InputDevice('/dev/input/event3')

sc = servo.Servo()

j0 = 4
j1 = 1
j2 = 0
j3 = 3

A = 304
B = 305
X = 307
Y = 308
start = 315
select = 314
LG = 317
RG = 318
LB = 310
RB = 311
LT = 312
RT = 313

def reset():
    sc.Kat(j0, 0)
    sc.Kat(j1, 0)
    sc.Kat(j2, 0)
    sc.Kat(j3, 0)
def Ruch(servo_id, event_value, inc):
    ret = ''
    if event_value > 0:
        ret = sc.IncKat(servo_id, inc)
    elif event_value < 0:
        ret = sc.IncKat(servo_id, inc * -1)    
    if ret <> '':
        print "servo %d = %d stopni" % (servo_id, ret)
reset()
try:
    for event in gamepad.read_loop():
        if event.type == ecodes.EV_KEY:
                if event.code == select:
                    sc.kill()              
                    GPIO.cleanup()
                if event.code == RT:
     	  	   sc.Kat(j3, 90)
                if event.code == LT: 
        	   sc.Kat(j3, -90)
                if event.code == start:
                    reset()
        elif event.type == ecodes.EV_ABS:
            absevent = categorize(event)
        	if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_HAT0X”:
                	if absevent.event.value == -1:
                    		inc = 3
                    		Ruch(j1, event.value, inc)
                    		time.sleep(.5)
                	elif absevent.event.value == 1:
                    		inc = 3
                    		Ruch(j1, event.value, inc)
                    		time.sleep(.5)
          	elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_HAT0Y":
                	if absevent.event.value == -1:
                    		inc = 1
                    		Ruch(j2, event.value, inc)
                    		time.sleep(.5)
                	elif absevent.event.value == 1:
                    		inc = 2
                   		Ruch(j2, event.value, inc)
                    		time.sleep(.5)
            	if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":
   			if absevent.event.value == 0:  
				inc = 5
                        	Ruch(j0, 1, inc)
				time.sleep(.5)
                    elif absevent.event.value == 255:
                        	inc = 5    
                        	Ruch(j0, -1, inc)
              			time.sleep(.5)
except KeyboardInterrupt:
    pass
reset()
sc.kill()
GPIO.cleanup()
