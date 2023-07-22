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

Zasilanie układu wraz z eksploatacją urządzenia wyczerpuje się, a do poprawnego funkcjonowania robota wymagane jest, aby wartość napięcia dostarczanego na poszczególne elementy była stała. Raspberry Pi wymaga 5V, a napięcie zasilania silnika wynosi 12V. Z rozwiązań dostępnych na rynku najlepszym było zastosowanie dwóch przetwornic prądu stałego, jedną typu step down, która utrzymywałaby stałe napięcie zadawane na mikrokontroler oraz drugą step up dla zwiększania napięcia do 12V dla silników krokowych. Moduł przetwornicy step down może służyć do zasilania dowolnych urządzeń o poborze prądu nie większym niż 5A. Przetwornica posiada woltomierz o dokładności 0,01V. Zastosowane przełączniki pozwalają na przełączanie pomiaru napięcia między wyjściem a wejściem. Płynna regulacja napięcia wyjściowego odbywa się za pomocą potencjometru wieloobrotowego.

![drv](https://github.com/Qruliq/RobotOmniWithArm/blob/main/pics/drv.png)

DRV8825 zapewnia zintegrowane rozwiązanie sterownika silnika dla drukarek, skanerów i innych zautomatyzowanych aplikacji sprzętowych, w tym również może spełniać rolę napędu dla kół w robocie mobilnym. Sterownik DRV8825 wyposażony jest w potencjometr do regulowania maksymalnego prądu. Układ scalony sterownika DRV8825 ma maksymalny prąd znamionowy 2,5A na cewkę, ale rezystory wykrywania prądu dodatkowo ograniczają maksymalny prąd do 2,2A, a rzeczywisty prąd, który jest dostarczany, zależy od chłodzenia IC. Płytka drukowana nośnika jest zaprojektowana tak, aby odprowadzać ciepło z układu scalonego, ale aby dostarczać więcej niż około 1,5A na cewkę, wymagany jest radiator lub inna metoda chłodzenia. Do chłodzenia układu, został wykorzystany radiator. W celu zabezpieczenia sterownika i silnika przed uszkodzeniem oraz aby oszczędzić zasilanie płynące z ogniw koniecznym było ustawienie ograniczenia prądu na sterowniku DRV8825. Po zapoznaniu się ze specyfikacją silnika oraz kilku testach, ograniczenie prądowe na każdym z czterech silników zostało ustawione na 1A.

![drv1](https://github.com/Qruliq/RobotOmniWithArm/blob/main/pics/drv1.png)

* **PCB**

![pcb1](https://github.com/Qruliq/RobotOmniWithArm/blob/main/pics/pcb1.png)

W celu uproszczenia sterowania układami wykonawczymi robota została zaprojektowana i wydrukowana płytka drukowana. Model płytki PCB jest uproszczoną wersją modułów HAT stosowanych w mikrokontrolerach Raspberry. HAT oznacza Hardware attached on top, co można przetłumaczyć na Sprzęt dołączony na górze. W podstawowym zarysie, nakładki Hat mają postać prostokątnych płytek drukowanych o wymiarach 65mm x 56mm z zaokrąglonymi narożami i otworami, za pomocą których nakładka daje się przykręcić na śruby do obudowy. Na płytce znajduje się 40-pinowe złącze GPIO kompatybilne z Raspberry Pi. Automatyczna konfiguracja jest zapewniona poprzez wyprowadzenia ID_SD oraz ID_SC, które łączą się z pamięcią EEPROM za pomocą interfejsu I2C. Wbudowana pamięć EEPROM, zawiera oprogramowanie konfiguracyjne dla poszczególnych wyprowadzeń GPIO oraz plik zawierający opis płytki HAT, który pozwala systemowi Linux na automatyczną instalację oprogramowania zawierającego wymagane sterowniki.

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
