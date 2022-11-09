"""Python module dictionaries exercises"""
# pylint: disable=invalid-name

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

quantity = {
  "Baby Spinach": 1,
  "Hot Chocolate": 3,
  "Crackers": 2,
  "Bacon": 1,
  "Carrots": 4,
  "Oranges": 2
}

for item, price in groceries.items():
    total = quantity[item] * price
    print(f"{quantity[item]} {item} @ ${price} = ${total:.2f}")
