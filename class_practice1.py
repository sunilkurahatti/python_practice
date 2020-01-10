# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 11:18:00 2020

@author: sunil
"""

movie_one={
'name':'xyz',
'director':'abc'
}

class movie:
	def __init__(self,new_name,new_director):
		self.name=new_name
		self.director=new_director


	def print_movie_info(self):
		return "<<{}>>, by {}".format(self.name,self.director)


my_movie={
'name':'bahubali',
'director':'dummy_bali'
}

new_movie=movie(my_movie['name'],my_movie['director'])
print(new_movie.name)
print(new_movie.director)
print(new_movie.print_movie_info())
