# -*- coding: utf-8 -*-
"""task2a.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19C9VUhlC9KbygghfVLsJAeQkT9gZsZo5
"""

file_in=open('input2a.txt','r')
file_out=open('output2a.txt','w')
total_case1=int(file_in.readline())
list1=list(map(int,file_in.readline().split(' ')))
total_case2=int(file_in.readline())
list2=list(map(int,file_in.readline().split(' ')))
new_list=list1+list2 #for the total list
new_list.sort() #sorting the values

#for the exact format as sample output
for i in range(len(new_list)):
  if i!=len(new_list)-1:
    file_out.write(f'{new_list[i]} ')
  else:
    file_out.write(f'{new_list[i]}')
file_out.close()