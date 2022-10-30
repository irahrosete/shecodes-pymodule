"""Python module functions exercises"""
# pylint: disable=invalid-name

# Q1. Write a function that takes a temperature in fahrenheit and returns
# the temperature in celsius.
# def fahrenheit_to_celsius(temp):
#     """Convert Fahrenheit to Celsius"""
#     celsius = (temp - 32) * 5 / 9
#     return celsius

# print(fahrenheit_to_celsius(32))

# Q2. Write a function that accepts one parameter (an integer) and returns True
# when that parameter is odd and False when that parameter is even.
def odd_or_even(num):
    """Returns False when odd or True when even"""
    if num % 2 == 0:
        return True
    else:
        return False

print(odd_or_even(8))
