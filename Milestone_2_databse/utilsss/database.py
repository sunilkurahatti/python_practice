"""
store data in text file in csv format
format will be : name,author,read
"""

import sqlite3


# books_file = 'books_file.json'


def file_open():
    connection = sqlite3.Connection("Data.db")
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS BOOKS (name text primary key, author text, read integer)')
    connection.commit()
    connection.close()


def add_book(name, author):
    connection = sqlite3.Connection("Data.db")
    cursor = connection.cursor()
    cursor.execute('INSERT INTO BOOKS VALUES (?,?,0)', (name, author))
    connection.commit()
    connection.close()


def get_all_books():
    connection = sqlite3.Connection("Data.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM BOOKS')
    books = [{'name':row[0],'author':row[1], 'read':row[2]} for row in cursor.fetchall()]
    connection.commit()
    connection.close()
    return books


def mark_as_read(name):
    connection = sqlite3.Connection("Data.db")
    cursor = connection.cursor()
    cursor.execute('UPDATE BOOKS SET read=1 where name=(?)', (name,))
    connection.commit()
    connection.close()


def delete_book(name):
    connection = sqlite3.Connection("Data.db")
    cursor = connection.cursor()
    cursor.execute('DELETE FROM BOOKS where name=(?)', (name,))
    connection.commit()
    connection.close()
