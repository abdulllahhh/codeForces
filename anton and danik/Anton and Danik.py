# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 07:39:35 2022

@author: babda
"""


n =int(input())
string = str(input())
a=0
d=0
for i in range(n):
    if(string[i] == 'A'):
        a = a + 1
    else:
        d = d + 1
if a>d:
    print("Anton")
if d>a :
    print("Danik")
if d==a :
    print("Friendship")

"""
n = int(input())
a_cnt = 2 * input().count('A')
print('Friendship' if n == a_cnt else ['Anton', 'Danik'][n > a_cnt])
profissional solution that i liked
"""

