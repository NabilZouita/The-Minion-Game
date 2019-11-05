# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 15:14:00 2019

@author: nzouita
"""
import re
from itertools import chain, combinations


def ConsonantsVowels(string):
    vowels = []
    constants = []
    for i in range(len(string)):
        if ((string[i] in ['a','e','i','o','u']) or (string[i] in ['A','E','I','O','U'])):
            vowels.append(string[i])
        else:
            constants.append(string[i])
    

    return (vowels, constants)
    
def substringSearch(string):    
    s = list(string)
    statement = list(map("".join, chain.from_iterable(combinations(s, r) for r in range(len(s)+1))))
    statement.remove(statement[0])
    #print("Current combination is : {}".format(statement))
    newList = []
    for i in range(len(statement)):
        if (statement[i] in string):
            newList.append(statement[i])

    #print("List after changes: {}".format(newList))
    #print(len(newList))
            
    newList = list(dict.fromkeys(newList))
    #print(newList)
    
    indexList = []
    for i in range(len(newList)):
        indexList.append([m.start() for m in re.finditer(newList[i],string)])
        
    
    #print(indexList)

#### Find all substring occurences in a string ###            
#import re
#[m.start() for m in re.finditer('test', 'test test test test')]

    return (newList, indexList)            


def winnerGame(string):
    kevin = 0
    stuart = 0
    stringList = substringSearch(string)[0]
    occList = substringSearch(string)[1]
    for i in range(len(stringList)):
        if (stringList[i][0] in ['A','E','I','O','U']):
            kevin += len(occList[i])
        else:
            stuart += len(occList[i])
            
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

