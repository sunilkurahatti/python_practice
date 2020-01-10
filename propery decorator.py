# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 16:34:49 2020

@author: skurahatti
"""


class Student:
    def __init__(self,name,college):
        self.name=name
        self.college=college
        self.marks=[]
        
        
    def average(self):
        return sum(self.marks)/len(self.marks)
    
    
class Working_student(Student):
    def __init__(self,name,college,salary):
        super().__init__(name,college)
        self.salary=salary
        
    @property 
    def weekly_sal(self):
        return self.salary*40
    
    
    

w_bob=Working_student('bod','vtu',40)
w_bob.marks.append(98)
w_bob.marks.append(89)

print(w_bob.average())
print(w_bob.weekly_sal)
