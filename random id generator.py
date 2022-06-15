# Viktor Nagels
import uuid
import csv
import sys

output = ""
length_uuid = 16
total = 50000

with open('uuid.csv', 'w', encoding='UTF8', newline="") as csvfile:
    fieldnames = ['uuid']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(0, total):
        writer.writerow(
            {'uuid': uuid.uuid4().hex[:length_uuid].upper()})
