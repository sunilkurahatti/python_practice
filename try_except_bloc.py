# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 17:37:33 2020

@author: sunil
"""
class Car:
    def __init__(self,name,make):
        self.name=name
        self.make=make
    def __repr__(self):
        "{}, {}".format(self.name,self.make)


class Garage:
	def __init__(self):
		self.cars=[]


	def __len__(self):
		return len(self.cars)


	def add_car(self,car):
		if not isinstance(car, Car):
			raise TypeError("tried to add {} but you can only add {}".format(car.__class__.__name__,Car.__class__))
		self.cars.append(car)




ford=Garage()

indica=Car('tata','indica')

try:
    if isinstance(indica,Car):
        ford.add_car(indica)
        print(len(ford))
except TypeError:
    print("type is not maching")
finally:
    print("we have came to end of program")





