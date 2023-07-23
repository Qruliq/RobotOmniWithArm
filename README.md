# RobotOmniWithArm
Omnikierunkowy robot mobilny z manipulatorem/Omnidirectional mobile robot with robot arm
![robot1](https://github.com/Qruliq/RobotOmniWithArm/blob/main/pics/robot1.jpg)

## About
Project inspired by a blog post on how to mechatronics: https://howtomechatronics.com/projects/arduino-robot-arm-and-mecanum-wheels-platform-automatic-operation/
![robot2](https://github.com/Qruliq/RobotOmniWithArm/blob/main/pics/robot2.jpg)

The construction includes a wooden (fiberboard) mobile platform and a 5DOF robot arm, which was printed from ABS filament. The platform is a 310mm x 180mm x 75mm. The design of the robot arm was taken from Ashing's "Robotic Arm" project, which was posted on the website [www.thingiverse.com](https://www.thingiverse.com/thing:994180). This raobot arm was used in this project under license CC BY-NC 4.0. By default, the robot arm has 5 degrees of freedom, but due to the kinematics of the platform, i.e. the fact that the robot can rotate around its axis, the rotating part of the arm hasn't been included in this project.
![robot3](https://github.com/Qruliq/RobotOmniWithArm/blob/main/pics/robot3.jpg)

## Construction and hardware
* **Construction**
  
![kola](https://github.com/Qruliq/RobotOmniWithArm/blob/main/pics/kola.png)

Mecanum wheels, commonly known as Swedish wheels, were invented in 1975 by Bengt Erland Ilon. By creating a platform equipped with a pair of this type of wheels for the left axle and a pair for the right one, and four DC motors as a drive for each wheel, we can obtain an omnidirectional robot with three degrees of freedom.

The wheels were mounted on shafts of stepper motors that were used to move the platform in all directions. To place the wheels on the drive, it was necessary to create additional WHA (Wheel hub assembly). The hubs used in the project were made of textolite and screwed through the central hole to the wheel, then the wheel with WHA was attached to the motor shaft and secured. The hub flange is 45mm and the shaft is 15mm.

![piasty](https://github.com/Qruliq/RobotOmniWithArm/blob/main/pics/piasty.png)

The construction of the robot requires four independently controlled motors. The main factor in the selection of the kinetic components was precision and compatibility with the power supply system. Due to the fact that stepper motors are known from its precision and simple structure. Stepper motor can be control by the angle of rotation work with low angular speeds and the ability to quickly change the direction of movement. From the stepper motors available on the market, the choice was four Nema 17 bipolar motors with a holding torque of 59Ncm.

![silniki](https://github.com/Qruliq/RobotOmniWithArm/blob/main/pics/silniki.png)

The same decision had to be made for robot arm. Since the robot arm used in the work is an implementation of an existing project, the selection of the drive for was dictated in advance. The choice was MG-995 or MG-996 servos from TowerPro. These servos have identical characteristics and seize, but different regulators. Due to the greater torque, the MG996R was used to control the arm, which is an improved version of the MG995 and offers better resistance and better precision.
* **Hardware**

![robot4](https://github.com/Qruliq/RobotOmniWithArm/blob/main/pics/robot4.png)

In the project was used Raspberry Pi 3 Model B+. Raspberry Pi can be powered by a variety of power supplies designed for smartphones. The Pi platform requires more power to operate than other devices with a micro-USB, because it requires a current of 700mA. Some power supplies are 500mA, which may cause performance issues. ZOP Power 11.1V 2800mAh 30C lithium-polymer cells have been implemented in the project. These cells have an excellent functional features, such as high durability. However, it is neccesery to careful while working with them. Improper use and mechanical damage can lead to explosion. The chemical compounds contained in lithium-based batteries are very hazardus, and fire outbreak cannot be extinguished with water. Many risks associated with the use of lithium-ion and lithium-polymer cells can be avoided by using dedicated chargers and by appropriate protection.

The power supply runs out as long as device is operational, plus the correct functioning it is required that the voltage supplied for the individual elements must be constant. The Raspberry Pi requires 5V and the stepper motor 12V. From the solutions available on the market, the best was to use two DC converters, one step down, which would maintain a constant voltage on the microcontroller and the second step up to increase the voltage to 12V for stepper motors. The step down converter module can be used to power any devices with a current consumption below 5A. 

![drv](https://github.com/Qruliq/RobotOmniWithArm/blob/main/pics/drv.png)

The DRV8825 provides an integrated motor driver solution for printers, scanners and other automated hardware applications, including the ability to drive the wheels of a mobile robot. The DRV8825 controller is equipped with a potentiometer to adjust the maximum current. The DRV8825 driver IC has a maximum current rating of 2.5A per coil, but current sensing resistors further limit the maximum current to 2.2A, and the actual current that is delivered depends on IC cooling. Driver PCB is designed to dissipate heat away from the IC, but a heat sink or other method of cooling is required to deliver more than about 1.5A per coil. A radiator was used to cool the system. In order to protect the controller and the motor from damage and to save power from the cells, it was necessary to set the current limit on the DRV8825 controller. After reviewing the motor specifications and some tests, the current limit on each of the four motors was set to 1A.

![drv1](https://github.com/Qruliq/RobotOmniWithArm/blob/main/pics/drv1.png)

* **PCB**

![pcb1](https://github.com/Qruliq/RobotOmniWithArm/blob/main/pics/pcb1.png)

In order to simplify the control of the robot's executive systems, a PCB was designed and printed. The PCB model is a simplified version of the HAT modules used in Raspberry microcontrollers. HAT stands for Hardware attached on top. In its basic outline, Hat overlays have the form of rectangular printed circuit board 65mm x 56mm with rounded corners and holes through which the overlay can be attached to the raspberry pi. The board has a 40-pin GPIO compatible with Raspberry Pi. Automatic configuration is provided by the ID_SD and ID_SC pins, which are connected to the EEPROM memory via I2C interface. EEPROM memory contains configuration software for individual GPIO pins and a file containing the description of the HAT board, which allows the Linux system to automatically install software containing the required drivers.

![pcb2](https://github.com/Qruliq/RobotOmniWithArm/blob/main/pics/pcb2.png)

The entire PCB design was made in EasyEDA, which is free online environment. The PCB has two layers of copper, top and bottom. The paths from the lower layer connect the STEP and DIR pins of the DRV8825 controllers with the corresponding Raspberry GPIO pins, connect the RST and SLP pins and connect motor power with power supply. A ground plane has been applied to the top layer. Only path that can be distinguished here are supplies 5V voltage to the servo pins and the FAULT pin of the DRV8825. The paths led to the M1, M2 and M3 pins of the stepper motor drivers were applied to the model in order to select the microstep resolution.  The value of 1/16 microstep was set for stepper motors of this robot. Using jumpers, M3 pin was connected with the 5V power supply. The next step was to solder the appropriate elements into its structure. Female pins were soldered into the places intended for the DRV8825 drivers and in the same fashion upper part were soldered, so that they coincide with the GPIO of the Raspberry Pi. Male pins are soldered into places where stepper motor phases, cables from servos, and setting microsteps on stepper motor drivers are connected. In addition, 100µf 35V decoupling capacitors and screw terminals to which 12V power is supplied are soldered into the board.

**PCB files are located: https://github.com/Qruliq/RobotOmniWithArm/tree/main/pcb**

## Control
* **Software**
  
The operating system used in this project is Raspbian. It is a free Debian-based operating system optimized for Raspberry Pi hardware. Raspbian is a set of basic programs and tools that make the Raspberry Pi works. In addition, it includes over 35,000 packages and pre-compiled software in an accessible format with simple installation process.
* **Code**

The robot control code was written in Python. There are a lot of libraries and functions offered by the Raspberry Pi and those were used in this project. One of the libraries that were used was Servoblaster. This is a library that provides an interface to control multiple (default 8) servos using GPIO pins. Thanks to the Servoblaster library, it is possible to control the position of the servo via PWM. The pulse width is maintained until a new command is sent to change it.Other libraries used in this project are pigpio library, with functions control the motors of the mobile platform and time library, whith its time stamps. To install the servoblaster on your microcontroller, the following operations must be prompt in the console window:
```
sudo apt-get install python-dev python-setuptools
git clone https://github.com/WiringPi/WiringPi-Python
cd WiringPi-Python
git submodule update --init
python setup.py install
cd .. 
```
The code can be found: https://github.com/Qruliq/RobotOmniWithArm/tree/main/code
* **Controls**

![pad](https://github.com/Qruliq/RobotOmniWithArm/blob/main/pics/pad.jpg)

The use of gamepads in ammature robotics is very common. It is easy to find solutions that map controller buttons while browsing ROS (Robot Operating System) packages. The most popular gamepad in roboticists is Playstation controller. The Gen Game K909 gamepad was used in the project. The device is designed for games for Android and IOS smartphones. The gamepad was used to control the mobile robot, because both the Raspberry Pi model B+ and the previously mentioned gamepad use Bluetooth. After pairing two devices with each other, it is important to map its buttons. The default path in raspbian is `/dev/input/`. To use a gamepad it is necessary to install the evdev library `sudo pip install evdev`. Then, using the code below it is possible to check what values ​​each button has.
```
#Code taken from https://core-electronics.com.au/guides/using-usb-and-bluetooth-controllers-with-python/
#import evdev
from evdev import InputDevice, categorize, ecodes

#creates object 'gamepad' to store the data
#you can call it whatever you like
gamepad = InputDevice('/dev/input/event3')

#prints out device info at start
print(gamepad)

#evdev takes care of polling the controller in a loop
for event in gamepad.read_loop():
    #filters by event type
    if event.type == ecodes.EV_KEY:
        print(event)
```

![konfiguracje](https://github.com/Qruliq/RobotOmniWithArm/blob/main/pics/konfiguracje.png)

The table below shows the direction of the wheels that should be given to each Swedish wheel, in order to move vehicle in ten different directions without changing its orientation as shown in the figure above. Number 1 in the table means that the wheel rotates forward, -1 means that it rotates backwards, and a value of 0 means that the wheel remains stationary. For example, to make a robot move right, the right wheels were rotated inward relative to each other, while the left wheels were rotated outward relative to each other. In order to obtain ten directions without changing robot's orientation, each of the wheels of the platform must maintain the same velocity.

| Direction | Wheel 0 | Wheel 1 | Wheel 2 | Wheel 3 |
|----------|--------|--------|--------|--------|
| Straight   |    1   |    1   |    1   |    1   |
| Backwards      |    -1   |    -1   |    -1   |    -1   |
| Left     |    -1   |    1   |    1   |    -1   |
| Right    |    1   |    -1   |    -1   |    1   |
| Diagonally Left-Straight |    0   |    1   |    1   |    0   |
| Diagonally Left-Backwards |    -1   |    0   |    0   |    -1   |
| Diagonally Right-Straight |    1   |    0   |    0   |    1   |
| Diagonally Right-Backwards |    0   |    1   |    1   |    0   |
| Rotate Left |    -1   |    1   |    -1   |    1   |
| Rotate Right |    1   |    -1   |    1   |    -1   |

## Final thoughts
Over the past decade, mobile robots have become very important field of robotics. The most popular mobile robots on the market are drones, RC toys and robotic vacuum cleaners. Access to the Internet, digitization, 3D printing and low prices of electronic parts make it possible to create mobile robots at home. Currently, robotics has spread to such an extent that robotics classes are conducted for early school students, competitions and competitions related to this field are organized and interesting projects can be easily found by browsing certain forums. The demand for such devices means that remotely controlled or autonomous models will bacome even more common.

Big shout out to Core Electronics, how to mechatronics and Ashing from www.thingiverse.com. Without them this project would not been finished. You are all truly wonderful.

**Videos presenting the robot can be found: https://github.com/Qruliq/RobotOmniWithArm/tree/main/video**
## Links
[1] https://howtomechatronics.com/projects/arduino-robot-arm-and-mecanum-wheels-platform-automatic-operation/

[2] https://core-electronics.com.au/guides/using-usb-and-bluetooth-controllers-with-python/

[3] https://www.thingiverse.com/thing:994180
