"""Python module oop exercises"""
# pylint: disable=invalid-name
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
import math

# Q1. Together, we wrote a class for a Book object. Update this class to add the ability to:
# 1. Go directly to a specific page number.
# 2. Bookmark a specific page number, i.e. not just the current page.
# 3. Automatically go back to the start of the book (i.e. page 1) when the user
# turns the final page.
class Book:
    def __init__(self, title, author, pages, current_page) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = current_page
        self.bookmark = 1

    def bookmark_page(self):
        self.bookmark = self.current_page

    # 1
    def turn_page(self):
        self.current_page += 1

    # 2
    def bookmark_specific_page(self, num):
        self.bookmark = num

    # 3
    def back_to_start(self):
        self.current_page = 1

    def go_to_page(self, num):
        self.current_page = int(num)

    def __str__(self) -> str:
        return (
            f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, "
            f"Current page: {self.current_page}"
        )

    def __len__(self):
        return self.pages

# my_book = Book("A great book", "me", 198, 1)
# my_book.go_to_page(3)
# my_book.bookmark_specific_page(23)
# print(my_book.current_page)
# print(my_book.bookmark)
# my_book.back_to_start()
# print(my_book.current_page)

# Q2. Write a class that represents a rectangle shape and has a method for each of the following:
# 1. Calculating the area.
# 2. Calculating the perimeter.
# 3. Calculating the length of the diagonal.
# 4. Determining whether or not the rectangle is a square.
class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = float(width)
        self.height = float(height)

    # 1
    def area(self):
        return self.width * self.height

    # 2
    def perimeter(self):
        return 2 * (self.width + self.height)

    # 3
    def diagonal_length(self):
        return round(math.sqrt(self.width**2 + self.height**2), 2)

    # 4
    def isSquare(self):
        return self.width == self.height

    def __str__(self) -> str:
        return f"This rectangle is {self.width} units wide and {self.height} units long."

# rect = Rectangle("2", 4)
# print(rect)
# print(rect.area())
# print(rect.perimeter())
# print(rect.diagonal_length())
# print(rect.isSquare())

# Q3. Part A Create a class to represent She Codes Students.
# Attributes that you may want to include:
# ● Name
# ● Program attended
# ● Year they attended
# Include a __str__ method to print a summary of the Student’s details.
# Part B What if a student has attended multiple programs?
# How would you adapt your class to handle this?
# A
class Student:
    def __init__(self, name, program, year) -> None:
        self.name = name
        self.program = program
        self.year = year

    def __str__(self) -> str:
        return (
            f"{self.name} attended {self.program} in {self.year}"
        )

# B
class Student2:
    def __init__(self, name, program_year) -> None:
        self.name = name
        self.program_year = program_year

    def __str__(self) -> str:
        new_line = "\n"
        return (
          f"{self.name} attended:\n"
          f"{''.join(f'  {key} in {value}{new_line}' for key, value in self.program_year.items())}"
        )

student = Student("Irah", "Javascipt", 2018)
print(student)
student2 = Student2("Irah", {"Python": 2022, "Django": 2021, "Java": 2019})
print(student2)
