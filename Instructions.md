
Properties

    - Team          F10 Фантомы
	- Team members: Ina Tix (Tikhamirova M.) - teamleader, technical engineer x Fire (Krasnov A.) - engineer x Timofey Kireev - computer vision engineer x Varya Yamchikova - computer vision engineer x Anna Komleva - computer vision engineer
	- Authors: Marina Tikhomirova x Alex Krasnov

## 1. Установка машины VMware

## 2. Установка GitHub Desktop
- регистрируемся на сайте github и скачиваем github desktop
- после скачивания заходим в github и создаем repository
- для его создания нажимаем на вкладку File и затем New repository
- задаем имя repository и пишим описание
- repository можно сделать приватным или публичным, а также можно добавить исключения в приватном repository
- создаем приватный repository, далее, заходим в окно settings, private repository и выбираем manage, после чего добавляем bart02
## 3. Выгрузка файлов из repository
- возвращаемся в окно code, после чего нажимаем на кнопку "Code" и выбираем "Download ZIP", в итоге скачается архив
## 3.1 Распаковка архива
- после скачивания архива его можно кланировать через командную строку, а также через github deskop. В нём мы выбираем окно "File", затем "Clone a repository" и затем его можно например кланировать через URL
## 4 VMware Workstation
- заходим в VWware
- выбираем окно "Open a Virtual Machine" или заходим в окно "File" и нажимаем "Open", или нажимаем сочетании клавиш "Ctrl + O" после чего выбираем Clover, который мы установили, а затем мы её импортируем
- В настройках меняем характеристики в них под свой компьютер (оперативную память, кол-во ядер, network adapter ставим на bridge, usb compatibility меняем на USB 2.0, в display можно вкл.чить 3D graphics, но это зависит от вашей видеокарты) 
- после включения виртуальной машины у нас появятся:
- 1. VS Coded - studio code в котором вы можете программировать сразу в python
- 2. QGroundControl - программа для прошивки и настройки дрона
- 3. Clover Drone Kit Tools - local host, он нужен для управления дроном, а также здесь можно посмотреть документацию, она работает без интернета
- 4. Gazebo - программа, в которой происходит сама симуляция.
## 4. Gazebo и написание программы
- заходим в gazebo 
- изначально из моделек (во вкладке Models) у нас стоят:
- 1 - паркет (пол)
- 2 - карта aruco маркеров
- 3 - clover
## 4.1 Информация о дроне
- 1 - заходим в Clover Drone Kit Tools
- 2 - далее заходим в "Topics" в которых можно найти информацию о состоянии дрона
## 4.2 Подготовка bash/python скрипта для настройки образа симулятора
- 





