"""Python module loops extended exercises"""
# pylint: disable=invalid-name

# Q1. Below is a list of foods and their prices per unit:
groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08]
]
# Ask the user how many units of each item they bought, then output the corresponding receipt.
# For the input below, assume that the input is provided in the same order as defined
# in the list above.
print("Enter quantity for each item.\n")

quantities = []
spinach = int(input("Baby Spinach > "))
choc = int(input("Hot Chocolate > "))
crackers = int(input("Crackers > "))
bacon = int(input("Bacon > "))
carrots = int(input("Carrots > "))
oranges = int(input("Oranges > "))

quantities.extend([spinach, choc, crackers, bacon, carrots, oranges])

for item in groceries:
    for q in quantities:
        item.append(q)

total = 0
print("\n====Izzy's Food Emporium====")
for item in groceries:
    amount = round(item[1] * item[2], 2)
    print(f"{item[0]:<20}${amount}")
    total += amount
print("============================")
print(f"\t\t    ${total}")

# Q2. Ask the user to enter a string. Output the string one character
# at a time, as well as it’s position in the string.
string = input("Please enter a string: ")
for i, letter in enumerate(string):
    print(f"{i:<3}{letter}")

# Q3. Ask the user for a number and use this to generate a pyramid of that height.
size = int(input("Pyramid size: "))

for i in range(size + 1):
    if i != 0:
        print(i * "*")

# Q4. Ask the user for a number and use this to generate a (different) pyramid of that height.
size = int(input("Pyramid size: "))
size_list = [1]

for i in range(size + (size - 1)):
    if i % 2 != 0:
        size_list.append(i + 2)

space_length = len(size_list)
for item in size_list:
    space_length -= 1
    spaces = space_length * " "
    asterisk = item * "*"
    print(f"{spaces}{asterisk}")
