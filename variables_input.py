"""Python module variable and user input exercises"""

# Q1. Write a program that takes two numbers
# from the user, and outputs their sum.
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
print(num1 + num2)

# Q2. Write a program that takes two numbers from the user,
# and outputs the equation representing the multiplication of the two numbers.
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
answer = num1 * num2
print(f"{num1} * {num2} = {answer}")

# Q3. Write a program that takes a distance in kilometers
# from the user, and output the distance in meters and centimeters.
km = input("How many kilometres? ")
m = float(km) * 1000
cm = float(km) * 100000
print(f"{float(km)}km = {int(m)}m")
print(f"{float(km)}km = {int(cm)}cm")

# Q4. Write a program that takes the users name
# and height (in centimeters), and outputs a summary sentence.
name = input("What is your name? ")
height = input("How tall are you (cms)? ")
print(f"{name} is {height}cms tall.")
