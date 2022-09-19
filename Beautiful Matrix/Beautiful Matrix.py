# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 08:01:06 2022

@author: babda
"""
a_init= [[]]
for i in range(1):
    a_init[i] = input().split('\n')

def BM(a):
    rowOf1=0
    colzOf1=0
    steps = 0
    newList = [[]*5]*5

    for i in range(5):
        newList[i]=a[0][i].split(' ')
        
    
    for k in range(5):
        for f in range(5):
            if (newList[k][f]=='1'):
                rowOf1,colzOf1=(k,f)
                break
               
    while(rowOf1 != 3):
        if(rowOf1 > 3):
           rowOf1 = rowOf1 -1
           steps = steps + 1
        elif(rowOf1 < 3):
           rowOf1 = rowOf1 +1
           steps = steps + 1
           
           
    while(colzOf1 != 3):
        if(colzOf1 > 3):
           colzOf1 = colzOf1 -1
           steps = steps + 1
        elif(colzOf1 < 3):
           colzOf1 = colzOf1 +1
           steps = steps + 1   
    return steps


BM(a_init)    