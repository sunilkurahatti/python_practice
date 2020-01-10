# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 16:23:01 2020

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
        
        
    def weekly_sal(self):
        return self.salary*40
    
    
    

w_bob=Working_student('bod','vtu',40)
w_bob.marks.append(98)
w_bob.marks.append(89)

print(w_bob.average())
print(w_bob.weekly_sal())

s_sam=Student('sam','bvvb')
s_sam.marks.append(56)
s_sam.marks.append(90)
print("\n")
print(s_sam.average())
print(s_sam.college)
print(s_sam.weekly_sal())#this will give error because normal student will not have salary