# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 19:06:00 2018

@author: Reece
"""

spam = ['a', 'b', 'c', 'd']

def listAnd(list):
    result = ''
    for x in range(len(list)-1):
        result += list[x]
        result += ', '
    result += 'and '
    result += list[len(list)-1]
    return result
        
print(listAnd(spam))