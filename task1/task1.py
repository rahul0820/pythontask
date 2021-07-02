import json
import csv

with open('task1.json') as json_file:
    data = json.load(json_file)
 
personal_data = data['Personal_Details']
 
new_file = open('new_file.csv', 'w')
 
csv_writer = csv.writer(new_file)
 
count = 0
 
for info in personal_data:
    if count == 0:
 
        header = info.keys()
        csv_writer.writerow(header)
        count += 1
 
    csv_writer.writerow(info.values())
 
new_file.close()