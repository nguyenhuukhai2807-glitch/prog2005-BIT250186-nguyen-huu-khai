import csv

with open('data.csv', mode='r') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        print(f'Mã: {row[0]}, Tên: {row[1]}, Tuổi: {row[2]}')
