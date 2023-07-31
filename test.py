import csv

with open('/home/student/Desktop/data.csv','rt')as f:
    data = csv.reader(f)
    for row in data:
        print(row)