import csv

# Данные для хеширования по имени корабля
alf = sorted('1234567890-_qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMйцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁё')
d = {alf[i]:i+1 for i in range(len(alf))}
# функция хеширования
def hash(s):
    s = s.replace(' ','')
    p = 123
    m = (10**9)+9
    i = 0
    hash_value = 0
    for c in s:
        hash_value += d[c] *p **i
        i+=1
    return int(hash_value % m)

# Открываем файл и записываем новый
with open('space.csv',encoding='utf-8') as f, open('space_new5.csv','w',newline='') as nf:
    data = list(csv.reader(f,delimiter=','))
    res = csv.writer(nf,delimiter=';')
    res.writerow(data[0])
    # меняем имя корабля на его хеш
    for stroka in data[1:]:
        name = stroka[0]
        h = hash(name)
        stroka[0] = h
        res.writerow(stroka)
