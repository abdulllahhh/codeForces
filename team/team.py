# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 07:20:17 2022

@author: babda
"""
solve = 0
list1 = []
n = int(input())
for i in range(n):
    list1.append(input())
for i in range(n):
    if(list1[i].count('1')>=2):
        solve  = solve + 1
print(solve)