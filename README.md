# RobotOmniWithArm
Omnikierunkowy robot mobilny z manipulatorem/Omnidirectional mobile robot with robot arm
![robot1](https://github.com/Qruliq/RobotOmniWithArm/blob/main/pics/robot1.jpg)

## About
Projekt inspired by a blog post on how to mechatronics: https://howtomechatronics.com/projects/arduino-robot-arm-and-mecanum-wheels-platform-automatic-operation/
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

Cały projekt płytki drukowanej został wykonany w darmowym środowisku internetowym EasyEDA. PCB ma dwie warstwy miedzi: dolną i górną . Ścieżki z dolnej warstwy łączą piny STEP oraz DIR sterowników DRV8825 z odpowiadającymi im pinom GPIO Raspberry, zwierają piny RST oraz SLP oraz doprowadzają 12V napięcie zasilania silników. W warstwie górnej została zastosowana płaszczyzna masy. Wyróżnić tu można jedynie ścieżkę która doprowadza napięcie 5V na piny serwa oraz pin FAULT sterownika DRV8825. Ścieżki poprowadzone na piny M1, M2 i M3 sterowników silników krokowych zastały naniesione na model w celu dobrania rozdzielczości mikrokroku. Tak jak przedstawiono to na Rys. 2.9. silniki naszego robota ustawiamy na wartość 1/16 mikrokroku. Za pomocą jumperów spinamy pin M3 z zasilaniem 5V. Kolejnym krokiem było wlutowanie w jej strukturę odpowiednich elementów. Piny damskie zostały wlutowane w miejsca przeznaczone dla sterowników DRV8825 oraz w górnej części płytki prototypowej, w ten sposób, aby pokrywały się z GPIO Raspberry Pi. Piny męskie wlutowano w miejsca, gdzie podłączane są fazy silników krokowych, przewody z serwomechanizmów, oraz ustawianie mikrokroków na sterownikach silników krokowych. Dodatkowo w płytkę wlutowano kondensatory odsprzęgające 100µf 35V oraz zaciski śrubowe na które doprowadzane jest zasilanie 12V. 
**Pliki dotyczące PCB znajdują się: https://github.com/Qruliq/RobotOmniWithArm/tree/main/pcb**

## Sterowanie
* **Oprogramowanie**
  
Systemem operacyjnym wykorzystanym w pracy jest Raspbian. Jest to darmowy system operacyjny oparty na Debianie, zoptymalizowany pod kątem sprzętu Raspberry Pi. Raspbian to zestaw podstawowych programów i narzędzi, dzięki którym Raspberry Pi działa. Ponadto zawiera ponad 35000 pakietów oraz wstępnie skompilowane oprogramowanie w przystępnym formacie, ułatwiające instalację na Raspberry Pi.
* **Kod**

Język Python został wykorzystany w pracy do napisania kodu sterowania robotem. Wykorzystano przy tym biblioteki oraz funkcje jakie oferuje Raspberry Pi. Jedną z bibliotek jakie zostały zastosowane był Servoblaster. Jest to biblioteka, która zapewnia interfejs do sterowania wieloma (domyślnie 8) serwami za pomocą pinów GPIO. Dzięki bibliotece Servoblaster możliwa jest kontrola pozycji serwa, poprzez wysyłanie polecenia do sterownika informującego o szerokości impulsu określonego na wyjściu serwomechanizmu. Szerokość impulsu jest utrzymywana do momentu wysłania nowego polecenia zmieniającego go. W pracy wykorzystano również bibliotekę pigpio, której funkcje posłużyły do sterowania silnikami platformy mobilnej, a także bibliotekę time, dzięki której można stosować stemple czasowe. Aby zainstalować servoblaster u siebie na mikrokontrolerze należy w oknie konsoli przeprowadzić następujące operacje:
```
sudo apt-get install python-dev python-setuptools
git clone https://github.com/WiringPi/WiringPi-Python
cd WiringPi-Python
git submodule update --init
python setup.py install
cd .. 
```
Kod do sterowania znajduje się: https://github.com/Qruliq/RobotOmniWithArm/tree/main/code
* **Sterowanie**

![pad](https://github.com/Qruliq/RobotOmniWithArm/blob/main/pics/pad.jpg)

Użycie gamepadów w robotyce hobbystycznej jest dość częstym zjawiskiem. Przeglądając pakiety środowiska ROS (Robot Operating System) można znaleźć rozwiązania, które mapują przyciski kontrolera. Najczęściej robotycy w swoich projektach wykorzystują kontrolery do konsoli Playstation. W projekcie został wykorzystany gamepad Gen Game K909. Urządzenie przeznaczone jest do gier na smartfony z systemem Android oraz IOS. Gamepad został wykorzystany do sterowania robotem mobilnym, ponieważ zarówno Raspberry Pi model B+, jak i wcześniej wymieniony gamepad wykorzystują technologie Bluetooth. Po sparowaniu ze sobą dwóch urządzeń istotnym jest zmapowanie jego przycisków. Domyślną ścieżką w przypadku raspbian jest `/dev/input/`. Aby wykorzystać gamepad w naszym projekcie należy w pierwszej kolejności zainstalować bibliotekę evdev `sudo pip install evdev`. Następnie za pomocą poniższego kodu sprawdzamy jakie wartości mają poszczególne przyciski.
```
#Kod zaczerpnięty z https://core-electronics.com.au/guides/using-usb-and-bluetooth-controllers-with-python/
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

Poniższa tabela przedstawia kierunek obrotu kół jaki powinien być zadany na każde koło szwedzkie, tak aby pojazd mógł poruszać się w dziesięciu różnych kierunkach bez zmiany swojej orientacji tak jak jest to przedstawione na powyższym rysunku. Wartość 1 w tabeli oznacza, że koło obraca się do przodu, wartość -1 to obrót do tyłu, natomiast gdy wartość jest równa 0 oznacza że koło pozostaje w bezruchu. Przykładowo, aby wykonać ruch poprzeczny w prawo, prawe koła były obracane względem siebie do wewnątrz, podczas gdy lewe koła były obracane względem siebie na zewnątrz. Warunkiem do uzyskania dziesięciu kierunków ruchu robota bez zmiany jego orientacji jest również utrzymanie takiej samej prędkości na każdym z kół platformy

| Kierunek | Koło 0 | Koło 1 | Koło 2 | Koło 3 |
|----------|--------|--------|--------|--------|
| Prosto   |    1   |    1   |    1   |    1   |
| Tył      |    -1   |    -1   |    -1   |    -1   |
| Lewo     |    -1   |    1   |    1   |    -1   |
| Prawo    |    1   |    -1   |    -1   |    1   |
| Lewa skośna do przodu|    0   |    1   |    1   |    0   |
| Lewa skośna do tyłu|    -1   |    0   |    0   |    -1   |
| Prawa skośna do przodu|    1   |    0   |    0   |    1   |
| Prawa skośna do tyłu|    0   |    1   |    1   |    0   |
| Obrót w lewo|    -1   |    1   |    -1   |    1   |
| Obrót w prawo|    1   |    -1   |    1   |    -1   |

## Podsumowanie
W ciągu ostatniej dekady roboty mobilne stały się coraz bardziej powszechne. Najbardziej popularnymi robotami na rynku są drony, zabawki RC oraz odkurzacze automatyczne. Powszechny dostęp do Internetu, cyfryzacja, druk 3D oraz niskie ceny części elektronicznych sprawia, że w warunkach domowych możliwym jest tworzenie robotów mobilnych. Obecnie robotyka rozpowszechniła się w takim stopniu, że zajęcia z robotyki są prowadzone dla młodzieży wczesnoszkolnej, organizowane są zawody i konkursy związane z tą dziedziną, a przeglądając fora tematyczne można z łatwością znaleźć intersujące projekty. Zapotrzebowanie na takie urządzenia sprawia, że tworzone są konstrukcje sterowane zdalnie, czy też modele autonomiczne, które cechują się szerokim zastosowaniem. 

Ogromne podziękowania dla Core Electronics, how to mechatronics i urzytkownika Ashing z www.thingiverse.com, którzy swoją twórczością przyczynili się do powstania tego robota. Filmy prezentujące działenie robota znajdują się: https://github.com/Qruliq/RobotOmniWithArm/tree/main/video

## Linki
[1] https://howtomechatronics.com/projects/arduino-robot-arm-and-mecanum-wheels-platform-automatic-operation/

[2] https://core-electronics.com.au/guides/using-usb-and-bluetooth-controllers-with-python/

[3] https://www.thingiverse.com/thing:994180
