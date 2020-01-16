"""
store data in text file in csv format
format will be : name,author,read
"""

books_file = 'books_file.txt'


def file_open():
    with open(books_file, 'w'):
        pass


def add_book(name, author):
    with open(books_file, 'a') as file:
        file.write("{},{},{}\n".format(name, author, '0'))


def get_all_books():
    with open(books_file, 'r') as file:
        return [line.strip().split(',') for line in file.readlines()]


def mark_as_read(name):
    books = get_all_books()
    for book in books:
        if book[0] == name:
            book[2] = '1'
    _save_book_file(books)


def _save_book_file(books):
    with open(books_file, 'w') as file:
        for book in books:
            file.write("{},{},{}\n".format(book[0], book[1], book[2]))


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book[0] != name]
    _save_book_file(books)
