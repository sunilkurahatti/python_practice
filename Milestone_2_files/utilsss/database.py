"""
store data in text file in csv format
format will be : name,author,read
"""

books_file = 'books_file.txt'


def add_book(name, author):
    with open(books_file, 'a') as file:
        file.write("{},{},{}\n".format(name, author, '0'))


def get_all_books():
    with open(books_file, 'r') as file:
        for line in file.readlines():
            lines = line.strip().split(',')
            print(lines)
            for i in lines:
                print(i)
            print({'name': lines[0], 'author': lines[1], 'read': lines[2]})
            print(i)
            boo = ["{'name':{}, 'author':{}}".format(line[0], line[1]) for line in lines]
            print(boo)
    # lines =[{"name:{},author:{},read:{}"}.format(line[0], line[1], line[2])
    # return "name:{},author:{},read:{}".format(line[0], line[1], line[2])


def mark_as_read(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True


def delete_book(name):
    books = [book for book in books if book['name'] != name]
