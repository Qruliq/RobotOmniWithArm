# RobotOmniWithArm
Omnikierunkowy robot mobilny z manipulatorem/Omnidirectional mobile robot with robot arm
![robot1](https://github.com/Qruliq/RobotOmniWithArm/blob/main/pics/robot1.jpg)

## O projekcie
Projekt został zainspirowany wpisem na blogu how to mechatronics: https://howtomechatronics.com/projects/arduino-robot-arm-and-mecanum-wheels-platform-automatic-operation/
![robot2](https://github.com/Qruliq/RobotOmniWithArm/blob/main/pics/robot2.jpg)

Konstrukcja składa się z drewnianej (płyta pilśniowa) platformy mobilnej oraz manipulatora 5DOF który zastał wydrukowany z filamentu ABS. Platofrma jest prostopadłościanem o wymiarach 310mm x 180mm x 75mm. Projekt manipulatora został zaczerpnięty z projektu „Robotic Arm” użytkownika Ashing, który został opublikowany na stronie internetowej [www.thingiverse.com](https://www.thingiverse.com/thing:994180 ). Projekt manipulatora podlega licencji CC BY-NC 4.0. Domyślnie w projekcie manipulator ma 5 stopni swobody, ale z uwagi na kinematykę podwozia tj. fakt że robot może obracać się wokół własnej osi, część obrotowa ramienia została pominięta.  
![robot3](https://github.com/Qruliq/RobotOmniWithArm/blob/main/pics/robot3.jpg)

## Budowa i hardware
* **Konstrukcja**
  
![kola](https://github.com/Qruliq/RobotOmniWithArm/blob/main/pics/kola.png)

Koła mecanum, potocznie nazywane kołami szwedzkimi, zostały opatentowane w 1975r. przez Bengta Erlanda Ilona. Tworząc konstrukcję platformy wyposażonej w parę kół przeznaczonych na lewą oś i parę na prawą oraz cztery silniki prądu stałego jako napęd każdego z kół, możemy uzyskać robota omnikierunkowego, posiadającego trzy stopnie swobody. 

Koła zostały zamontowane na wałkach silników krokowych, które zostały użyte do przemieszczania się platformy we wszystkich kierunkach. Do umieszczenia kół na napędzie, było konieczne stworzenie dodatkowych piast. Piasty użyte w pracy zostały wykonane z tekstolitu i przykręcone wkrętem przez otwór centralny do koła, następnie całość została nałożona na wałek napędowy silnika i zabezpieczona. Kołnierz piasty ma 45mm, natomiast wałek 15mm.

![piasty](https://github.com/Qruliq/RobotOmniWithArm/blob/main/pics/piasty.png)

Platforma składa się z czterech kół mecanum oraz tej samej liczby silników. Koła mecanum są z kolei przymocowane do wałów poszczególnych silników za pomocą piast. Konstrukcja obiektu wymaga zastosowania czterech niezależnie sterowanych silników. Głównym czynnikiem podczas doboru układu wykonawczego podwozia była precyzja oraz kompatybilność z układem zasilającym. Z uwagi, że silniki krokowe są napędami precyzyjnymi o prostej budowie, a także charakteryzuje je możliwość kontroli kąta obrotu, praca na niskich prędkościach kątowych oraz zdolność do szybkiej zmiany kierunku ruchu, zostały one wybrane jako napęd podwozia. Z dostępnych na rynku silników krokowych, w pracy zostały użyte cztery silniki bipolarne Nema 17 z momentem trzymania 59Ncm.

![silniki](https://github.com/Qruliq/RobotOmniWithArm/blob/main/pics/silniki.png)

Oprócz platformy mobilnej, niezbędne było wybranie układu wykonawczego dla manipulatora. Ponieważ manipulator wykorzystany w pracy jest implementacją gotowego projektu, również dobór napędu do niego był podyktowany z góry. Sterowanie manipulatorem można było oprzeć o serwa MG-995 lub MG-996 firmy TowerPro. Są to bliźniacze serwa, które mają identyczne charakterystyki i wymiary, lecz różne regulatory. Ze względu na większy moment, do sterowania manipulatorem został wykorzystany MG996R, który jest ulepszoną wersją MG995, oferując przy tym lepszą odporność na wstrząsy oraz większą precyzję. 
* **Hardware**

![robot4](https://github.com/Qruliq/RobotOmniWithArm/blob/main/pics/robot4.png)

W projekcie wykorzystano Raspberry Pi 3 Model B+
