# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 08:24:38 2023

@author: babda
"""

def solution (lst,integer):
    result = []
    len_lst = len(lst)
    maxx = 0
    for i in range(len_lst):
        count_for_each_element = 1
        for j in range(len_lst):
            # if(j == i ):
            #     continue
            if(lst[i] in result):
                continue
            elif(abs(lst[i] - lst[j]) == integer):
                    result.append(lst[i])
                    count_for_each_element = count_for_each_element + 1
        if(count_for_each_element > maxx):
            maxx = count_for_each_element
            
    return maxx
res = solution([3,2,4,1,6], 2)