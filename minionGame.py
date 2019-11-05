# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 15:14:00 2019

@author: nzouita
"""
from itertools import chain, combinations, permutations
#import itertools
import re

def ConsonantsVowels(string):
    vowels = []
    constants = []
    for i in range(len(string)):
        if ((string[i] in ['a','e','i','o','u']) or (string[i] in ['A','E','I','O','U'])):
            vowels.append(string[i])
        else:
            constants.append(string[i])
    
    #print([vowels,constants])
    #var = [vowels,constants]
#    print(vowels, constants)
    
    return (vowels, constants)
    
def substringSearch(string):    
    s = list(string)
    statement = list(map("".join, chain.from_iterable(combinations(s, r) for r in range(len(s)+1))))
    statement.remove(statement[0])
    print("Current combination is : {}".format(statement))
    newList = []
    for i in range(len(statement)):
        if (statement[i] in string):
            newList.append(statement[i])

    print("List after changes: {}".format(newList))
    print(len(newList))
            
    newList = list(dict.fromkeys(newList))
    print(newList)
            
### Remove all duplicates ###
#mylist = ["a", "b", "a", "c", "c"]
#mylist = list(dict.fromkeys(mylist))
#print(mylist)

    return newList            


def winnerGame(string):
    kevin = 0
    stuart = 0
    newList = substringSearch(string)
    for i in range(len(newList)):
        if (newList[i][0] in ['A','E','I','O','U']):
            kevin += 1
        else:
            stuart += 1
            
    if (kevin > stuart):
        print("{} {}".format("Kevin", kevin))
    elif (stuart > kevin):
        print("{} {}".format("Stuart", stuart))
    else:
        print("Draw")
            
            
    
    
if __name__ == '__main__':
    s = input()
    ConsonantsVowels(s)
    substringSearch(s)
    winnerGame(s)

### Two possible tries ###
#    var = Consonants&Vowels(string)
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
# var = Consonants&Vowels[0]
# var2 = Consonants&Vowels[1]

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