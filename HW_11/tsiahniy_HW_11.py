import time
class Vehicle():

       logo = '__________________________________________________\n' \
              '__________________________________________¶_______\n' \
              '_________________________________________¶¶_______\n' \
              '_________________________________________¶¶¶______\n' \
              '_______________________¶¶________________¶¶¶______\n' \
              '_____________________¶¶¶_________________¶¶¶______\n' \
              '________________¶___¶¶_¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_\n' \
              '________________¶_______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_\n' \
              '________________¶¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶\n' \
              '_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶\n' \
              '_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶__¶¶¶¶¶¶¶¶¶¶\n' \
              '_____¶¶¶¶¶¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_\n' \
              '____¶¶¶_¶¶¶____¶¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_\n' \
              '___¶¶__¶¶¶¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_\n' \
              '¶¶_¶___¶¶¶¶¶¶¶¶_¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_\n' \
              '¶¶¶¶___¶¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶_\n' \
              '_______¶¶¶¶___¶¶____¶¶¶¶¶_____________¶¶__¶¶_¶¶¶__\n' \
              '________¶¶¶¶¶¶¶¶____¶¶¶¶______________¶¶¶__¶¶_¶¶__\n' \
              '_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶________________¶¶¶_¶_¶¶¶__\n' \
              '___________¶¶¶¶¶¶¶¶¶____________________¶¶¶¶¶¶¶___'


class Car(Vehicle):
       logo = '__________________________________________________\n' \
              '__________________________________________¶_______\n' \
              '_________________________________________¶¶_______\n' \
              '_________________________________________¶¶¶______\n' \
              '_______________________¶¶________________¶¶¶______\n' \
              '_____________________¶¶¶_________________¶¶¶______\n' \
              '________________¶___¶¶_¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_\n' \
              '________________¶_______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_\n' \
              '________________¶¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶\n' \
              '_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶\n' \
              '_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶__¶¶¶¶¶¶¶¶¶¶\n' \
              '_____¶¶¶¶¶¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_\n' \
              '____¶¶¶_¶¶¶____¶¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_\n' \
              '___¶¶__¶¶¶¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_\n' \
              '¶¶_¶___¶¶¶¶¶¶¶¶_¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_\n' \
              '¶¶¶¶___¶¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶_\n' \
              '_______¶¶¶¶___¶¶____¶¶¶¶¶_____________¶¶__¶¶_¶¶¶__\n' \
              '________¶¶¶¶¶¶¶¶____¶¶¶¶______________¶¶¶__¶¶_¶¶__\n' \
              '_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶________________¶¶¶_¶_¶¶¶__\n' \
              '___________¶¶¶¶¶¶¶¶¶____________________¶¶¶¶¶¶¶___'


class Plane(Vehicle):
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

       logo1 = logo.splitlines()
       def run(self):
              for i in logo1:
                     time.sleep(0.1)
                     print(i)
              time.sleep(1)
              print('БЖЖЖЖЖЖЖЖЖЖ')

planer = Plane
planer.run(self=planer)

