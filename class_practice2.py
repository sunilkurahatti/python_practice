# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Club:
    def __init__(self,name):
        self.name=name
        self.players=[]
        
    def __getitem__(self, i):
        return self[i]
    
    def __len__(self):
        return len(self.players)
    
    def __str__(self):
        return f"club {self.name} has {len(self)} players"
    
    def __repr__(self):
        return f"club {self.name} has {len(self)} players"
    
    
    
    
    
    
    
    
my_club=Club('one')
my_club.players.append('sunil')
my_club.players.append('anil')
print(my_club.name)
print(my_club.players)
print(my_club.players[1])
print(len(my_club.players))
print(my_club)
