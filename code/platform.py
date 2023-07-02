import time
import pigpio
from evdev import InputDevice, categorize, ecodes

gamepad = InputDevice('/dev/input/event3')

DIR2 = 21     
STEP2 = 20   
DIR1 = 5     
STEP1 = 12    
DIR3 = 13     
STEP3 = 6    
DIR4 = 26     
STEP4 = 19   
pi = pigpio.pi()
pi.set_mode(DIR1, pigpio.OUTPUT)
pi.set_mode(STEP1, pigpio.OUTPUT)
pi.set_mode(DIR2, pigpio.OUTPUT)
pi.set_mode(STEP2, pigpio.OUTPUT)
pi.set_mode(DIR3, pigpio.OUTPUT)
pi.set_mode(STEP3, pigpio.OUTPUT)
pi.set_mode(DIR4, pigpio.OUTPUT)
pi.set_mode(STEP4, pigpio.OUTPUT)

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

def przod():
    pi.set_PWM_dutycycle(STEP1, 128)
    pi.set_PWM_frequency(STEP1, 500)
    pi.set_PWM_dutycycle(STEP2, 128)
    pi.set_PWM_frequency(STEP2, 500)
    pi.set_PWM_dutycycle(STEP3, 128) 
    pi.set_PWM_frequency(STEP3, 500)  
    pi.set_PWM_dutycycle(STEP4, 128)  
    pi.set_PWM_frequency(STEP4, 500)  
    pi.write(DIR1, 1)  
    pi.write(DIR2, 1)  
    pi.write(DIR3, 1)  
    pi.write(DIR4, 1)
    time.sleep(0.1)
def tyl():
    pi.set_PWM_dutycycle(STEP1, 128)
    pi.set_PWM_frequency(STEP1, 500)
    pi.set_PWM_dutycycle(STEP2, 128) 
    pi.set_PWM_frequency(STEP2, 500)
    pi.set_PWM_dutycycle(STEP3, 128)
    pi.set_PWM_frequency(STEP3, 500)
    pi.set_PWM_dutycycle(STEP4, 128)
    pi.set_PWM_frequency(STEP4, 500)
    pi.write(DIR1, 0)  
    pi.write(DIR2, 0) 
    pi.write(DIR3, 0)  
    pi.write(DIR4, 0)
    time.sleep(0.1)
def prawo():
    pi.set_PWM_dutycycle(STEP1, 128)  
    pi.set_PWM_frequency(STEP1, 500)  
    pi.set_PWM_dutycycle(STEP2, 128)  
    pi.set_PWM_frequency(STEP2, 500)  
    pi.set_PWM_dutycycle(STEP3, 128)  
    pi.set_PWM_frequency(STEP3, 500)  
    pi.set_PWM_dutycycle(STEP4, 128)  
    pi.set_PWM_frequency(STEP4, 500)    
    pi.write(DIR1, 0)
    pi.write(DIR2, 1) 
    pi.write(DIR3, 1)  
    pi.write(DIR4, 0)  
    time.sleep(0.1)
def lewo():
    pi.set_PWM_dutycycle(STEP1, 128) 
    pi.set_PWM_frequency(STEP1, 500)
    pi.set_PWM_dutycycle(STEP2, 128)  
    pi.set_PWM_frequency(STEP2, 500)  
    pi.set_PWM_dutycycle(STEP3, 128) 
    pi.set_PWM_frequency(STEP3, 500)
    pi.set_PWM_dutycycle(STEP4, 128)
    pi.set_PWM_frequency(STEP4, 500)
    pi.write(DIR1, 1)  
    pi.write(DIR2, 0)  
    pi.write(DIR3, 0)  
    pi.write(DIR4, 1)  
    time.sleep(0.1)
def psg():
    pi.set_PWM_dutycycle(STEP1, 0)  
    pi.set_PWM_frequency(STEP1, 500) 
    pi.set_PWM_dutycycle(STEP2, 128)  
    pi.set_PWM_frequency(STEP2, 500)  
    pi.set_PWM_dutycycle(STEP3, 128)  
    pi.set_PWM_frequency(STEP3, 500)  
    pi.set_PWM_dutycycle(STEP4, 0)  
    pi.set_PWM_frequency(STEP4, 500)  
    pi.write(DIR2, 1)  
    pi.write(DIR3, 1) 
    time.sleep(0.1)
def lsg():
    pi.set_PWM_dutycycle(STEP1, 128)  
    pi.set_PWM_frequency(STEP1, 500)  
    pi.set_PWM_dutycycle(STEP2, 0) 
    pi.set_PWM_frequency(STEP2, 500)  
    pi.set_PWM_dutycycle(STEP3, 0) 
    pi.set_PWM_frequency(STEP3, 500)  
    pi.set_PWM_dutycycle(STEP4, 128)  
    pi.set_PWM_frequency(STEP4, 500)  
    pi.write(DIR1, 1)  
    pi.write(DIR4, 1)  
    time.sleep(0.1)
def psd():
    pi.set_PWM_dutycycle(STEP1, 128) 
    pi.set_PWM_frequency(STEP1, 500)  
    pi.set_PWM_dutycycle(STEP2, 0)  
    pi.set_PWM_frequency(STEP2, 500)  
    pi.set_PWM_dutycycle(STEP3, 0)  
    pi.set_PWM_frequency(STEP3, 500) 
    pi.set_PWM_dutycycle(STEP4, 128)  
    pi.set_PWM_frequency(STEP4, 500)  
    pi.write(DIR1, 0)  
    pi.write(DIR4, 0)  
    time.sleep(0.1)
def lsd():
    pi.set_PWM_dutycycle(STEP1, 0) 
    pi.set_PWM_frequency(STEP1, 500)  
    pi.set_PWM_dutycycle(STEP2, 128)  
    pi.set_PWM_frequency(STEP2, 500)  
    pi.set_PWM_dutycycle(STEP3, 128)  
    pi.set_PWM_frequency(STEP3, 500)  
    pi.set_PWM_dutycycle(STEP4, 0)  
    pi.set_PWM_frequency(STEP4, 500) 
    pi.write(DIR2, 0)  
    pi.write(DIR3, 0)  
    time.sleep(0.1)
def op():
    pi.set_PWM_dutycycle(STEP1, 128)  
    pi.set_PWM_frequency(STEP1, 500)  
    pi.set_PWM_dutycycle(STEP2, 128)  
    pi.set_PWM_frequency(STEP2, 500) 
    pi.set_PWM_dutycycle(STEP3, 128) 
    pi.set_PWM_frequency(STEP3, 500)  
    pi.set_PWM_dutycycle(STEP4, 128) 
    pi.set_PWM_frequency(STEP4, 500) 
    pi.write(DIR1, 1)  
    pi.write(DIR2, 1)  
    pi.write(DIR3, 0)  
    pi.write(DIR4, 0)  
    time.sleep(0.1)
def ol():
    pi.set_PWM_dutycycle(STEP1, 128)  
    pi.set_PWM_frequency(STEP1, 500)  
    pi.set_PWM_dutycycle(STEP2, 128)  
    pi.set_PWM_frequency(STEP2, 500)  
    pi.set_PWM_dutycycle(STEP3, 128)  
    pi.set_PWM_frequency(STEP3, 500)  
    pi.set_PWM_dutycycle(STEP4, 128)  
    pi.set_PWM_frequency(STEP4, 500)  
    pi.write(DIR1, 0)  
    pi.write(DIR2, 0)  
    pi.write(DIR3, 1) 
    pi.write(DIR4, 1)  
    time.sleep(0.1)
def reset():
    pi.set_PWM_dutycycle(STEP1, 0)  
    pi.set_PWM_dutycycle(STEP2, 0)  
    pi.set_PWM_dutycycle(STEP3, 0)  
    pi.set_PWM_dutycycle(STEP4, 0)  
reset()
try:
    for event in gamepad.read_loop():
        if event.type == ecodes.EV_KEY:
                if event.code == RB:
                    op()
                    time.sleep(.1)
                if event.code == LB:
                    ol()
                    time.sleep(.1)
                else:
                    reset()
        elif event.type == ecodes.EV_ABS:
            absevent = categorize(event)
            if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":
                if absevent.event.value == 0:
                    lewo()
                elif absevent.event.value == 255:
                    prawo()
                else:
                    reset()
            if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Y":
                if absevent.event.value == 0:
                    przod()    
                elif absevent.event.value == 255:
                    tyl()
                else:
                    reset()
            if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RZ":
                if absevent.event.value == 0:
                    psd()
                elif absevent.event.value == 255:
                    lsd()
                else:
                    reset()      
            if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Z":
                if absevent.event.value == 0:
                    psg()
                elif absevent.event.value == 255:
                    lsg()
                else:
                    reset() 
except KeyboardInterrupt:
    pass

reset()
