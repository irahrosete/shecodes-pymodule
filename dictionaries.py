"""Python module dictionaries exercises"""
# pylint: disable=invalid-name
import csv

# Q1. The dictionary below represents the cost of individual items in a supermarket.
# A separate dictionary is given in the table below, this dictionary represents the
# quantity of each item purchased. Use these two dictionaries to write a program that
# outputs the cost of each item.
groceries = {
  "Baby Spinach": 2.78,
  "Hot Chocolate": 3.70,
  "Crackers": 2.10,
  "Bacon": 9.00,
  "Carrots": 0.56,
  "Oranges": 3.08
}

# quantity = {
#   "Baby Spinach": 1,
#   "Hot Chocolate": 3,
#   "Crackers": 2,
#   "Bacon": 1,
#   "Carrots": 4,
#   "Oranges": 2
# }
quantity = {
  "Baby Spinach": 2,
  "Hot Chocolate": 1,
  "Crackers": 4,
  "Bacon": 0,
  "Carrots": 8,
  "Oranges": 5
}

# for item, price in groceries.items():
#     total = quantity[item] * price
#     print(f"{quantity[item]} {item} @ ${price} = ${total:.2f}")

# alternative:
# for item in groceries:
#     total = quantity[item] * groceries[item]
#     print(f"{quantity[item]} {item} @ ${groceries[item]} = ${total:.2f}")

# Q2. The dictionary below contains several colour names and a counter (defaulted to 0).
# Your task is to iterate over a list of colours and keep track of the number of times
# each colour has occurred by updating the corresponding counter in this dictionary.
colour_counts = {
    "blue": 0,
    "green": 0,
    "yellow": 0,
    "red": 0,
    "purple": 0,
    "orange": 0,
  }

# colours = [
#     "purple",
#     "red",
#     "yellow",
#     "blue",
#     "purple",
#     "orange",
#     "blue",
#     "purple",
#     "orange",
#     "green"
# ]

colours = [
    "orange",
    "purple",
    "blue",
    "yellow",
    "green",
    "green",
    "purple",
    "purple",
    "green",
    "blue",
    "green",
    "orange",
    "purple",
    "blue",
    "green",
    "orange",
    "orange",
    "red",
    "yellow",
    "yellow"
]

# for item, counter in colour_counts.items():
#     for colour in colours:
#         if colour == item:
#             counter = counter + 1
#     print(f"{item}: {counter}")

# Q3. Given the list of names below, create a dictionary where each key is a name and the value
# is the number of times that name occurs in the list.
# names = [
#     "Maddy", "Bel", "Elnaz", "Gia", "Izzy",
#     "Joy", "Katie", "Maddie", "Tash", "Nic",
#     "Rachael", "Bec", "Bec", "Tabitha", "Teagen",
#     "Viv", "Anna", "Catherine", "Catherine", "Debby",
#     "Gab", "Megan", "Michelle", "Nic", "Roxy",
#     "Samara", "Sasha", "Sophie", "Teagen", "Viv"
# ]

names = [
"Miranda", "Sophie", "Emily", "Taylor", "Anne",
"Djuarli", "Anika", "Rosie", "Miranda", "Taylor",
"Abby", "Sarah", "Teagen", "Abby", "Abby",
"Maddie", "Miranda", "Rosie"
]

# names_count = {}

# for name in names:
#     if names_count.get(name) is None:
#         names_count[name] = 1
#     else:
#         names_count[name] += 1

# for name, count in names_count.items():
#     print(name, count)

# Q4. Read the colour data from colours_20_simple.csv and save the data in a dictionary where
# the key is the hex code and value is the corresponding English name.
colour_hex = {}

with open("csv_files/colours_20_simple.csv", encoding="utf8") as colours_file:
    reader = csv.reader(colours_file)
    next(reader)
    for line in reader:
        colour_hex.update({line[1]: line[2]})

for hexcode, colour in colour_hex.items():
    print(f"{hexcode}: {colour}")
