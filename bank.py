import requests
import datetime


res = requests.request('GET', 'https://belarusbank.by/api/kursExchange?city=Брест')
print(res.headers['Date'])
otdel = {}
for dct in res.json():
    for key, val in dct.items():
        if key == 'filials_text':
            otdel[val] = dct
    dct.pop('filial_id')
    dct.pop('info_worktime')
    dct.pop('street_type')
    dct.pop('filials_text')
    dct.pop('home_number')
    dct.pop('name')
    dct.pop('name_type')
    dct.pop('street')
    dct.pop('sap_id')



for otd in otdel.keys():
    print(otd)

def choise():
    while True:
        user_choice = input('Выберете отбеление ---> ": ')
        user_choice = user_choice.strip()
        if user_choice not in otdel.keys():
            print('Не верный ввод')
            continue
        else:
            return user_choice

user_choice = choise()
choise_otdel =otdel[user_choice]

for k, v in choise_otdel.items():
    print(k, v)


with open('logs.txt', mode='at') as logs:
    data = (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S \n'))
    otdl = f'{user_choice} \n'
    msg = f'\n' \
          f'{data} {otdl}'
    logs.write(msg)
    for k, v in choise_otdel.items():
        log = f'{k} - {v} \n'
        logs.write(log)


