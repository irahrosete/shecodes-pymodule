"""Python module oop exercises"""
# pylint: disable=invalid-name
# pylint: disable=missing-function-docstring

# Q1. Together, we wrote a class for a Book object. Update this class to add the ability to:
# 1. Go directly to a specific page number.
# 2. Bookmark a specific page number, i.e. not just the current page.
# 3. Automatically go back to the start of the book (i.e. page 1) when the user
# turns the final page.
class Book:
    """Book class"""
    def __init__(self, title, author, pages, current_page):
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

    def __str__(self):
        return (
            f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, "
            f"Current page: {self.current_page}"
        )

    def __len__(self):
        return self.pages

my_book = Book("A great book", "me", 198, 1)
my_book.go_to_page(3)
my_book.bookmark_specific_page(23)
print(my_book.current_page)
print(my_book.bookmark)
my_book.back_to_start()
print(my_book.current_page)
