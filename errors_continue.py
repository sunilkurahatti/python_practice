# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 13:00:23 2020

@author: sunil
"""

def interact():
    while True:
        try:
            user_input=int(input("Please entre a integer"))
            is_even=user_input%2==0
            if is_even==0:
                print("{}, is even number".format(user_input))
            else:
                print("{}, is odd number".format(user_input))
        except ValueError:
            print("A Value error has occured please enter valid intiger")
        finally:
            user_input=input("do you want to play this game again: ")
            if user_input!='y':
                print("Goodbye")
                break


interact()