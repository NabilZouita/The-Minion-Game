# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 15:14:00 2019

@author: nzouita
"""
from itertools import chain, combinations, permutations
#import itertools
import re

def vowels_and_constants(string):
    vowels = []
    constants = []
    for i in range(len(string)):
        if ((string[i] in ['a','e','i','o','u']) or (string[i] in ['A','E','I','O','U'])):
            vowels.append(string[i])
        else:
            constants.append(string[i])
    
    #print([vowels,constants])
    #var = [vowels,constants]
    print(vowels, constants)
    
    return (vowels, constants)
    
def search_substrings(string):    
    s = list(string)
    statement = list(map("".join, chain.from_iterable(combinations(s, r) for r in range(len(s)+1))))
    statement.remove(statement[0])
    print("Current combination is : {}".format(statement))
    newList = []
    for i in range(len(statement)):
        if (statement[i] in string):
            newList.append(statement[i])
#        if (statement[i] not in string):
#            #del statement[i]
#            statement.remove(statement[i])
#            newList.append(statement[i+1])
#        elif (statement[i] in string):
#            newList.append(statement[i])
            
    print("List after changes: {}".format(newList))
    print(len(newList))
            
    
            
    
    
if __name__ == '__main__':
    s = input()
    vowels_and_constants(s)
    search_substrings(s)

### Two possible tries ###
#    var = vowels_and_constants(string)
##    print(var)
#    statement1 = list(map("".join, chain.from_iterable(combinations(var[0], r2) for r2 in range(len(var[1])+1))))
#    print(statement1) ### display combinations of elements from same lists
#    
    #### Use of zip method for all combinations of two lists ####
#    list1=['a','b','c']
#    list2=[1,2]
#
#    print(list([zip(x,list2) for x in itertools.permutations(list1,len(list2))])) ### display zip objects

### All possible permutation of two lists ###
#import itertools
#list1=['a','b','c']
#list2=[1,2]
#
#[zip(x,list2) for x in itertools.permutations(list1,len(list2))]

    
### Find a substring in a string ###
#import re
#[m.start() for m in re.finditer('test', 'test test test test')]

#### Old code ####
# var = vowels_and_constants[0]
# var2 = vowels_and_constants[1]

# for i in range(len(var) + len(var2)):
#     for j in range(len(var) + len(var2)):    
#         [m.start() for m in re.finditer(var[i]+var[j])]

## Print possible combination of a string ##""
# def powerset(iterable):
#     "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
#     s = list(iterable)
#     return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

# print(list(map(''.join, powerset('abcd'))))
    
### Old code ###
#print(constants)
#def minion_game(string):
    # your code goes here