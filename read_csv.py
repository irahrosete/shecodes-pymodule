"""Python module reading csv files exercises"""
# pylint: disable=invalid-name
import csv

#Q1. Write a program that reads in colours_20_simple.csv and output the colour data.
with open("csv_files/colours_20.csv", encoding="utf8") as colours_file:
    reader = csv.reader(colours_file)
    for line in reader:
        print(f"{line[1].lstrip():<12} {line[2].lstrip():<8} {line[4].lstrip()}")
