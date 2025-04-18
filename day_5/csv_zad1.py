# dane oddzielone przecinkiem lub innym znakiem podziału
import csv

fields = ['name', 'branch', 'year', 'cgpa']
row = ['Radek', 'coe', "3", "90"]

filename = 'records.csv'
with open(filename, "w", newline="") as fh:
    csvwriter = csv.writer(fh, delimiter=";")
    csvwriter.writerow(fields)
    csvwriter.writerow(row)

read_fields = []
read_rows = []

with open(filename, "r") as f:
    csvreader = csv.reader(f, delimiter=";")
    print(csvreader)

    read_fields = next(csvreader) # odczyt jedej linijki

    for row in csvreader: # odczyt od drugiej linijki
        read_rows.append(row)

print(read_fields)
print(5 * "-")
print(read_rows)
# 3 ['name', 'branch', 'year', 'cgpa']
# -----
# [['Radek', 'coe', '3', '90']]