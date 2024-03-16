import csv


# Открываем файл и записываем новый
with open('space.csv',encoding='utf-8') as f, open('space_new.txt','w',newline='') as nf:
    data = list(csv.reader(f,delimiter=','))
    res = csv.writer(nf,delimiter=';')


