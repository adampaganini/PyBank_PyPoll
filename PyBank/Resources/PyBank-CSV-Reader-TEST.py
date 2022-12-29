import os
import csv

#set wd path for file to be cross-platform w/ diff OSs
csv_path = os.path.join('..','Resources','budget_data.csv')

with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    print(csv_reader)

    #read header row first
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")

    #read each row
    for row in csv_reader:
        print(row)
