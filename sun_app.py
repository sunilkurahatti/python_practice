# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 12:46:38 2020

@author: skurahatti

"""
movies=[]

def menu():
    user_input=input("\nPlease enter 'a' to add movie, 'l' to list the movie, 'f' to find the movie and 'q' to quit: ")
    
    while user_input!='q':
        if user_input=='a':
            add_movie()
        elif user_input=='l':
            list_movie(movies)
        elif user_input=='f':
            find_movie()
        else:
            print("Unknown-command please enter valid command")
        user_input=input("\nPlease enter 'a' to add movie, 'l' to list the movie, 'f' to find the movie and 'q' to quit: ")
    print("terminating program Thanks for stopping by")


def add_movie():
    name=input("Enter a movie name: ")
    director=input("Enter name of director: ")
    year=input("Enter the year of release: ")
    movies.append({
        'name':name,
        'director':director,
        'year':year
        })
    
def list_movie(movies_list):
    for x in movies_list:
        show_movie_name(x)
        
def show_movie_name(movie):
    print(f"name: {movie['name']}")
    print(f"director: {movie['director']}")
    print(f"year: {movie['year']}")
    
def find_movie():
    att_property=input("What attribute you are looking for: ")
    search_ed=input("Enter the search element: ")
    found_movies=find_by_attr(movies,search_ed,lambda x: x[att_property])
    list_movie(found_movies)
    
def find_by_attr(items,expected,finder):
    found=[]
    for i in items:
        if finder(i)==expected:
            found.append(i)
    return found


menu()

print(movies)