"""Python module while loops exercises"""

# Q1. Continuously ask the user to enter a number until they provide a blank input.
# Output the sum of all the numbers.
# message = input("Enter a number: ")
# total = 0

# while message != "":
#     if message != "":
#         total += int(message)
#     else:
#         break
#     message = input("Enter a number: ")
# else:
#     print(total)

# Q2. Ask the user to enter a number. Print all the odd numbers
# between 0 and that number (inclusive).
number = int(input("Enter a number: "))
num_list = []

for i in range(number + 1):
    num_list.append(i)

num_list.remove(0)

for item in num_list:
    while item % 2 == 0:
        break
    else:
        print(item)
