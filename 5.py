import csv

alf = sorted('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMйцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁё')
d = {alf[i]:i+1 for i in range(len(alf))}
def hash(s):
    s = s.replace(' ','')
    p = 71
    m = (10**9)+9
    i = 0
    hash_value = 0
    for c in s:
        hash_value += d[c] *p **i
        i+=1
    return int(hash_value % m)

# Открываем файл и записываем новый
with open('space.csv',encoding='utf-8') as f, open('space_new.txt','w',newline='') as nf:
    data = list(csv.reader(f,delimiter=','))
    res = csv.writer(nf,delimiter=';')
    res.writerow(data[0])
    for stroka in data[1:]:
        name = stroka[0]
        h = hash(fio)
        stroka[0] = h
        res.writerow(stroka)
