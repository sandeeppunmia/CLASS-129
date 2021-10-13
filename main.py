import csv

data=[]

with open("dataset_2.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data.append(row)
headers=data[0]
planet_data=data[:]
for data_point in planet_data:
    data_point[2]=data_point[2].lower()
planet_data.sort(key=lambda planet_data:planet_data[2])

with open("dataset2_sorted.csv","a+") as f:
    csvreader=csv.writer(f)
    csvreader.writerow(headers)
    csvreader.writerows(planet_data)