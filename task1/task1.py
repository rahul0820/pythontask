import json
import csv

with open('task1.json') as json_file:
    data = json.load(json_file)
 
personal_data = data['Personal_Details']
 
personal_data_file = open('personal_data_file.csv', 'w')
 
csv_writer = csv.writer(personal_data_file)
 
count = 0
 
for info in personal_data:
    if count == 0:
 
        header = info.keys()
        csv_writer.writerow(header)
        count += 1
 
    csv_writer.writerow(info.values())
 
personal_data_file.close()