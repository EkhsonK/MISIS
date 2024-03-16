import csv


# Перекодируем файл с помощью UTF-8
with open('space.csv',encoding='utf-8') as f, open('space_new.csv','w',newline='') as nf:
    data = list(csv.reader(f,delimiter=','))
    res = csv.writer(nf,delimiter=';')
    for i in data:
        res.writerow(i)


