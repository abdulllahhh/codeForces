# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 09:39:09 2022

@author: babda
"""

limak , bob = input().split()
limak = int(limak)
bob = int(bob)
years = 0
while(limak <= bob):
    years = years + 1
    limak = limak *3
    bob = bob * 2
print(years)