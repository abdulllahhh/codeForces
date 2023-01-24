# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 08:35:28 2022

@author: babda
"""
# input from user
list_size = int(input())
list_of_col_sizes = input().split()

# make a list of 1s like empty container
list_1s = [[1]*list_size for _ in range(int(max(list_of_col_sizes)))]

# the required boxes position
int_of_col_index=[] 

# turn list that we take as input to iter over it 
for item_of_each_column in list_of_col_sizes:
    int_of_col_index.append(int(item_of_each_column)) #list items into integers


#add 0s into the 1s list to specify the boxes
for cols in range(len(int_of_col_index)):
    for rows in range(0,int_of_col_index[cols]):
        rows_reversed = (rows +1) * -1
        list_1s[rows_reversed][cols] = 0

#sort rows decending
for row in range(int(max(list_of_col_sizes))):
    list_1s[row].sort(reverse=True)
    
#transform list   
tlist = list(zip(*list_1s))  

#put output in a list 
out=[]
for cols in range(list_size):
    out.append(tlist[cols][:].count(0))

# print output like without brackets and comas
index=0
for name in out:
    print(out[index], end=" ")
    index += 1






# list_1s[:][-(int(j)+1)]