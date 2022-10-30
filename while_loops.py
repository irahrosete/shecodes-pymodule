"""Python module while loops exercises"""

#Q1. Continuously ask the user to enter a number until they provide a blank input.
# Output the sum of all the numbers.

message = input("Enter a number: ")
total = 0

while message != "":
    if message != "":
        total += int(message)
    else:
        break
    message = input("Enter a number: ")
else:
    print(total)
