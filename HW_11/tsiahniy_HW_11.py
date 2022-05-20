import time


class Vehicle:

    speed = 0
    number_of_passengers = 0
    logo = '_______________$$$$$$$$$$$$$$$$$$$\n' \
           '______________$$$$_$$$$$$$$$$$$$$$$$\n' \
           '____________$$$$_________$$$_______$$$\n' \
           '___________$$$___________$$$_________$$$\n' \
           '__________$$$$___________$$$__________$$$$\n' \
           '__$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n' \
           '_$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n' \
           '_$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n' \
           '__$$$$$$$$$___$$$$$$$$$$$$$$$$$$$$$$$$$___$$$$$$$$\n' \
           '_$$$$$$$$_______$$$$$$$$$$$$$$$$$$$$$_______$$$$$$\n' \
           '__$$$$$$__$$$$$__$$$$$$$$$$$$$$$$$$$__$$$$$$__$$$\n' \
           '_________$$___$$_____________________$$___$$__\n' \
           '_________$$___$$_____________________$$$__$$__\n' \
           '__________$$$$_________________________$$$$__'

    def __init__(self, initial_speed, initial_number_of_passengers):
        self.speed = initial_speed
        self.number_of_passenger = initial_number_of_passengers


class Car(Vehicle):

    brand = ''

    def __init__(self, initial_speed, initial_number_of_passengers, initial_brand):
        super().__init__(initial_speed, initial_number_of_passengers)
        self.brand = initial_brand

    def run(self):
        '''
        Построчно рисуем лого
        '''
        logo1 = self.logo.splitlines()
        for i in logo1:
            time.sleep(0.1)
            print(i)
        time.sleep(1)
        print('')
        print('')
        print('БЗЗЗЗЗ')


class Plane(Vehicle):
    flight_range = 0
    logo = '____________________¶¶¶\n' \
           ' ___________________¶8_8¶¶8\n' \
           '___________________¶¶¶¶__8¶8\n' \
           '______________________8¶¶8_8¶8\n' \
           '________________________8¶¶8_8¶\n' \
           '__________________________¶¶¶8_¶8\n' \
           '___________________________¶88¶_¶¶\n' \
           '____________________________¶8_¶88¶\n' \
           '_____________________________¶__¶¶8¶8\n' \
           '_____________________________¶¶__8¶_¶8\n' \
           '______________________________¶____¶_¶8\n' \
           '______________________________¶_____¶_¶¶\n' \
           '______________________________¶8____8¶_¶8\n' \
           '______________________________8¶____8¶__¶88¶¶¶¶¶¶\n' \
           '______________________________8¶____¶____¶¶¶¶¶¶¶¶_88¶¶¶¶¶¶¶¶¶¶¶¶¶\n' \
           '______________________________8¶__8¶_____88¶¶¶¶¶¶¶88__________¶¶8¶¶¶\n' \
           '____________¶¶_________________8_¶¶___8¶¶¶¶88_________________¶____8¶\n' \
           '___________8¶¶¶_______________8¶¶¶8¶¶888_____________¶¶¶¶_____¶___8¶\n' \
           '___8________¶_¶¶________888¶¶8¶¶_____________________¶¶¶¶_8¶___¶¶¶¶\n' \
           '_¶¶¶8¶88____¶__¶___8¶¶¶¶8¶8___________________________¶¶__8¶¶¶¶¶8\n' \
           '__8¶¶¶¶8¶¶8_¶__¶¶¶888_______________________8¶¶__8¶¶¶¶¶¶¶¶¶¶8\n' \
           '____8¶¶8__8¶¶¶¶88________________________88¶¶¶¶¶¶¶¶¶8¶88\n' \
           '_______8¶¶___¶8_8_________8¶____888¶¶¶¶888¶¶888\n' \
           '__________¶¶¶___________88¶¶¶¶¶¶¶¶¶¶88__¶¶\n' \
           '___________¶¶__88¶¶¶¶¶¶¶¶8¶¶88¶¶_______¶¶\n' \
           '__________¶___¶¶¶¶¶8______¶____8¶8____¶¶\n' \
           '________8¶___¶¶__________¶8______¶___¶¶\n' \
           '_______¶¶__8¶8__________¶¶______¶¶__¶8__88¶8\n' \
           '____88¶8_8¶¶___________8¶______¶8__¶¶¶¶¶¶¶¶¶8\n' \
           '____¶¶¶¶¶8____________8¶_____¶¶___¶¶__8_¶¶_¶¶\n' \
           '_____________________¶¶____8¶8__¶¶_¶8_¶_¶¶¶¶¶\n' \
           '____________________¶¶___8¶¶__8¶8___88¶¶¶¶¶8\n' \
           '__________________8¶___8¶¶___¶¶\n' \
           '________________8¶8__8¶¶___¶¶8\n' \
           '_______________¶¶__¶¶8___¶¶8\n' \
           '_____________¶¶__¶¶8___¶¶8\n' \
           '___________8¶88¶¶___8¶¶8\n' \
           '_______88¶¶¶8¶8___8¶¶8\n' \
           '______¶¶¶88____8¶¶8\n' \
           '______¶¶___8¶¶¶8\n' \
           '________¶¶¶'

    def __init__(self, initial_speed, initial_number_of_passengers, initial_flight_range):
        super().__init__(initial_speed, initial_number_of_passengers)
        self.flight_range = initial_flight_range

    def run(self):
        '''
        Построчно рисуем лого
        '''
        logo1 = self.logo.splitlines()
        for i in logo1:
            time.sleep(0.1)
            print(i)
        time.sleep(1)
        print('')
        print('')
        print('БЖЖЖЖЖЖЖЖЖЖ')


class Ship(Vehicle):
    water_displacement = 0

    logo = '___________________¶¶¶8¶¶_________________________\n' \
           '_____________¶¶¶¶¶¶¶¶¶¶¶¶_________________________\n' \
           '_____________¶¶¶¶8¶¶¶¶¶¶¶_________________________\n' \
           '______________________¶¶__________________________\n' \
           '_____________________¶8¶_¶8¶______________________\n' \
           '_____________________¶8¶_¶888¶____________________\n' \
           '_____________________¶8¶__8¶¶8¶¶__________________\n' \
           '__________________¶¶_¶8¶__¶88¶¶8¶_________________\n' \
           '__________________¶8¶¶8¶___¶8888¶¶________________\n' \
           '_________________¶8¶¶¶¶¶___¶888¶88¶¶______________\n' \
           '_______________¶88¶¶¶¶8¶____¶8¶88¶¶¶¶_____________\n' \
           '______________¶¶8¶¶¶¶¶¶¶____¶8¶¶¶¶¶¶¶¶____________\n' \
           '_____________¶88888¶_¶¶¶____¶88¶8¶¶888¶¶__________\n' \
           '____________¶8888¶8¶_¶¶¶____¶88888¶¶8888¶_________\n' \
           '___________¶888¶888¶_¶8¶____¶8¶¶88¶888¶88¶________\n' \
           '__________¶8¶888888¶_¶8¶____¶8¶88¶8888$888¶_______\n' \
           '_________¶88¶¶88888¶_¶8¶____¶88¶88¶¶¶¶888¶8¶______\n' \
           '_______¶8888¶¶888¶¶¶_¶8¶_____8888¶8¶¶8888¶¶8¶_____\n' \
           '______¶88888¶8¶¶¶¶8¶_¶8¶____¶¶888¶¶¶88¶8¶888¶_____\n' \
           '____¶¶888¶¶¶8¶8¶¶88¶_¶¶¶____¶88888888¶8¶88888_____\n' \
           '__¶¶88¶88888888888¶¶_¶8¶___¶88888888¶88¶88¶88_____\n' \
           '_¶8¶¶¶¶¶¶_¶¶¶88888¶¶_¶8¶___88¶¶8¶¶¶¶¶¶¶¶¶¶¶¶¶_____\n' \
           '¶¶____________¶¶¶8¶¶_¶¶¶__¶88¶¶____________¶¶__¶¶_\n' \
           '888¶¶¶¶¶________¶¶8¶_¶¶¶__¶¶¶___________¶¶¶¶¶¶¶8¶¶\n' \
           '_¶¶¶888¶¶88¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶888¶¶¶¶___\n' \
           '____¶¶8¶¶8888888¶888888888$8888¶8888888888¶_______\n' \
           '_____¶¶8888¶¶8888888888¶888¶¶88¶¶88¶88888¶________\n' \
           '________¶¶¶¶¶¶888¶¶¶88888¶8888888¶8¶¶¶¶¶__________\n' \
           '______________888¶¶¶¶88¶¶8¶8¶¶¶8¶¶________________'

    def __init__(self, initial_speed, initial_number_of_passengers, initial_water_displacement):
        super().__init__(initial_speed, initial_number_of_passengers)
        self.water_displacement = initial_water_displacement

    def run(self):
        '''
        Построчно рисуем лого
        '''
        logo1 = self.logo.splitlines()
        for i in logo1:
            time.sleep(0.1)
            print(i)
        time.sleep(1)
        print('')
        print('')
        print('БУЛЬ - БУЛЬ')


abstract_planer = Plane(initial_speed=900, initial_number_of_passengers=120, initial_flight_range=8000)
abstract_car = Car(initial_speed=70, initial_number_of_passengers=4, initial_brand='BMW')
abstract_ship = Ship(initial_speed=40, initial_number_of_passengers=400, initial_water_displacement=30000)

print(f'скорость {abstract_planer.speed} км/ч\n'
      f'число пассажиров {abstract_planer.number_of_passenger} человек\n'
      f'дальность полёта {abstract_planer.flight_range} км')
abstract_planer.run()

print(f'скорость {abstract_car.speed} км/ч\n'
      f'число пассажиров {abstract_car.number_of_passenger} человек\n'
      f'марка автомобиля {abstract_car.brand}')
abstract_car.run()

print(f'скорость {abstract_ship.speed} км/ч\n'
      f'число пассажиров {abstract_ship.number_of_passenger} человек\n'
      f'водоизмещение {abstract_ship.water_displacement} м^3')
abstract_ship.run()





