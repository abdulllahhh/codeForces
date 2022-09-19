# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 07:53:30 2022

@author: babda
"""

inputList = []
myList =[]

for i in range(5):
    inputList = input().split()
    myList.append(inputList)
    
    
rowOfOne = 0
colOfOne = 0

for i in range(5):
    for j in range(5):
        if(myList[i][j] == '1'):
            rowOfOne = i
            colOfOne = j
            break
steps=0    
while(rowOfOne != 2):
    if(rowOfOne < 2):
        rowOfOne = rowOfOne +1
        steps = steps +1
    elif(rowOfOne >2)    :
        rowOfOne = rowOfOne - 1
        steps = steps +1
    
while(colOfOne != 2):
    if colOfOne < 2 :
        colOfOne = colOfOne +1
        steps = steps +1
    elif colOfOne > 2 :
        colOfOne = colOfOne - 1
        steps = steps +1
    
    
    
print(steps)    
    
    
    
    
    
    