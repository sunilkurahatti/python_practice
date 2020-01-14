"""
store data in text file in csv format
format will be : name,author,read
"""

books_file='books_file.txt'

def add_book(name,author):
    with open(books_file,'a') as file:
        file.write("[{},{},{}]\n".format(name,author,0))


def get_all_books():
    return books


def mark_as_read(name):
    for book in books:
        if book['name']==name:
            book['read']=True

def delete_book(name):
    global books
    books=[book for book in books if book['name']!=name ]