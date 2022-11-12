"""Python module databases lesson"""
# pylint: disable=invalid-name

import sqlite3

connection = sqlite3.connect("books.db")
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE book (
    id integer PRIMARY KEY,
    title TEXT,
    pages INTEGER,
    current_page INTEGER
    )
""")
cursor.execute("""
    INSERT INTO book VALUES (
    0, 'A great book', 213, 27
    )
""")
cursor.execute("""
    INSERT INTO book VALUES (
    1, 'Another great book', 395, 387
    )
""")
connection.commit()
rows = cursor.execute("SELECT title, pages, current_page FROM book")
for row in rows:
    print(row)
connection.close()

# run even when data already in db
cursor.execute("""
    CREATE TABLE IF NOT EXISTS book (
    id integer PRIMARY KEY,
    title TEXT,
    pages INTEGER,
    current_page INTEGER
    )
""")