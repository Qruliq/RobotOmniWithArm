import time
import os

servos = {}

class Servo:
    def __init__(self):
        os.system('sudo /home/pi/PiBits/ServoBlaster/user/servod')

    
    def Kat(self, servo_id, kat):

        if kat > 90:
            kat = 90
        elif kat < -90:
            kat = -90
        puls = 1520 + (kat * 400) / 45
        os.system("echo %d=%d > /dev/servoblaster"%(servo_id, puls/10))
        time.sleep(0.1)
        servos[servo_id] = kat
        return servos[servo_id]
        
    def IncKat(self, servo_id, inc):
        kat = servos.get(servo_id, 0)
        return self.Kat(servo_id, kat + inc)

    def kill(self):
        os.system('sudo killall servod')
