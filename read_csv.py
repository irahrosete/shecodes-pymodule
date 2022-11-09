"""Python module reading csv files exercises"""
# pylint: disable=invalid-name
import csv

# Q1. Write a program that reads in colours_20_simple.csv and output the colour data.
# with open("csv_files/colours_20.csv", encoding="utf8") as colours_file:
#     reader = csv.reader(colours_file)
#     for line in reader:
#         print(f"{line[1].lstrip():<12} {line[2].lstrip():<8} {line[4].lstrip()}")

# Q2. Write a program that reads in colours_20_simple.csv and outputs the colour data in order
# English, Hex then RGB.
with open("csv_files/colours_20_simple.csv", encoding="utf8") as colours_file:
    reader = csv.reader(colours_file)
    next(reader)
    for line in reader:
        print(f"{line[2]}, Hex: {line[1]}, RGB: {line[0]}")

# Q3. Write a program that reads in colours_20.csv and output the colour data in order
# English, Hex then RGB.
with open("csv_files/colours_20.csv", encoding="utf8") as colours_file:
    reader = csv.reader(colours_file)
    next(reader)
    for line in reader:
        print(f"{line[4]}, Hex: {line[2]}, RGB: {line[1]}")