import csv

data1 = csv.reader(open('rd_1.csv', 'r'))
data2 = csv.reader(open('rd_2.csv', 'r'))

list_1 = []
list_2 = []

for rows in data1:
    print(rows)
    if rows == 0:
        continue
    dic = (rows[0], rows[1])
    print(dic)

print(list_1)
