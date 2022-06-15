# Viktor Nagels
import uuid
import csv

length_uuid = 16
total = 20

with open('uuid.txt', 'w', encoding='UTF8') as csvfile:
    fieldnames = ['id', 'uuid']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(0, total):
        writer.writerow(
            {'id': i, 'uuid': uuid.uuid4().hex[:length_uuid].upper()})
