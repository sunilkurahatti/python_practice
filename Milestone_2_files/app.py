# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 14:14:28 2020

@author: skurahatti

"""
from utilsss import database

USER_CHOICE = """
Enter:
-'a' to add new book
-'l' to list all books
-'r' to mark book as read
-'d' to delete a book
-'q' to quit

your choices here:
"""


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("\nPlease enter a valid input")
        user_input = input(USER_CHOICE)


def prompt_add_book():
    name = input("Enter name of the book: ")
    author = input("Enter the author name: ")
    database.add_book(name, author)


def list_books():
    books = database.get_all_books()
    for book in books:
        print(book)
        # read ='YES' if book[2]=='1' else 'NO'
        print("{} written by {} read status is {}".format(book[0], book[1], book[2]))


def prompt_read_book():
    name = input("please enter name of the book to mak as read: ")
    database.mark_as_read(name)


def prompt_delete_book():
    name = input("Enter name of the book to delete: ")
    database.delete_book(name)

#
# books_file = 'books_file.txt'
#
# with open(books_file, 'r') as file:
#     lines = [line.strip().split(',') for line in file.readlines()]
#     print(lines)

menu()
