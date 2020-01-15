"""
store data in text file in csv format
format will be : name,author,read
"""

books_file = 'books_file.txt'


def add_book(name, author):
    with open(books_file, 'a') as file:
        file.write("{},{},{}\n".format(name, author, 0))


def get_all_books():
    with open(books_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]

    return [
        {'name': line[0], 'author': line[1], 'read': line[2]}
        for line in lines]


def mark_as_read(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True


def delete_book(name):
    books = [book for book in books if book['name'] != name]
