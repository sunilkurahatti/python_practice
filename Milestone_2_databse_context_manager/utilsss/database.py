"""
store data in text file in csv format
format will be : name,author,read
"""


from .database_connection import DatabaseConnection


def file_open():
    with DatabaseConnection('bob.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS BOOKS (name text primary key, author text, read integer)')


def add_book(name, author):
    with DatabaseConnection('bob.db') as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO BOOKS VALUES (?,?,0)', (name, author))


def get_all_books():
    with DatabaseConnection('bob.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM BOOKS')
        books = [{'name':row[0],'author':row[1], 'read':row[2]} for row in cursor.fetchall()]
    return books


def mark_as_read(name):
    with DatabaseConnection('bob.db') as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE BOOKS SET read=1 where name=(?)', (name,))


def delete_book(name):
    with DatabaseConnection('bob.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM BOOKS where name=(?)', (name,))
