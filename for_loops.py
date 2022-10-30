"""Python module for loops exercises"""

# Q1. Ask the user for a number. Use a for loop to print the times tables for that number.
num = int(input("Enter a number: "))
num_list = []

for i in range(num):
    num_list.append(i + 1)

for item in num_list:
    print(f"{num} * {item} = {num * item}")
