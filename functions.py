"""Python module functions exercises"""
# pylint: disable=invalid-name

# Q1. Write a function that takes a temperature in fahrenheit and returns
# the temperature in celsius.
def fahrenheit_to_celsius(temp):
    """Convert Fahrenheit to Celsius"""
    celsius = (temp - 32) * 5 / 9
    return celsius

print(fahrenheit_to_celsius(32))
