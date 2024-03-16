import csv

def search(name,data):
    for stroka in data:
        if stroka[0] == name:
            return stroka

with open('space.csv',encoding='UTF-8') as f:
    data = list(csv.reader(f,delimiter=','))
    name = input()
    while name != 'stop':
        stroka = search(name,data)
        if stroka is None:
            print('error.. er.. ror..')
        else:
            print(f"Корабль {stroka[0]} последний раз был на связи по координатам: {stroka[2]}, что составляет: космических единиц")
        name = input()