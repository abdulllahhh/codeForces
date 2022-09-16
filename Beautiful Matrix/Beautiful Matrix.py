# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 08:01:06 2022

@author: babda
"""
rowOf1=0
colzOf1=0
steps = 0
a = [[]]
for i in range(1):
    a[i] = input().split('\n')

[int(x) for i in a]


for k in range(5):
    for j in range(5):
        if (a[k][j]=='1'):
            rowOf1,colzOf1=(k,j)
            break
while(rowOf1 != 3):
    if(rowOf1>3):
       rowOf1 = rowOf1 -1
       steps = steps + 1
    elif(rowOf1<3):
       rowOf1 = rowOf1 +1
       steps = steps + 1
while(colzOf1 != 3):
    if(colzOf1>3):
       colzOf1 = colzOf1 -1
       steps = steps + 1
    elif(rowOf1<3):
       colzOf1 = colzOf1 +1
       steps = steps + 1   