"""
store data in text file in csv format
format will be : name,author,read
"""

import json
import os

books_file = 'books_file.json'


def file_open():
    os.curdir
    files = os.listdir(os.curdir)
    if books_file not in files:
        with open(books_file, 'w') as a_file:
            json.dump([], a_file)


def add_book(name, author):
    books = get_all_books()
    books.append({'name': name, 'author': author, 'read': False})
    _save_book_file(books)


def get_all_books():
    with open(books_file, 'r') as file:
        return json.load(file)


def mark_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = True
    _save_book_file(books)


def _save_book_file(books):
    with open(books_file, 'w') as file:
        json.dump(books, file)


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_book_file(books)
