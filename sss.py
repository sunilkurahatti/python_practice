# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 19:52:10 2020

@author: sunil
"""

class Car:
	def __init__(self,name,make):
		self.name=name
		self.make=make
     def __repr__(self):
         return "{},{}".format(self.name,self.make)
