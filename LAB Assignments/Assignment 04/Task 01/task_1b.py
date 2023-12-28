# -*- coding: utf-8 -*-
"""Task 1b.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ysf89-b7-MPYQ4HrZ3XnDP9cf4QymiMO
"""

file_in=open('input1b.txt','r')
file_out=open('output1b.txt','w')
temp=file_in.readline().split(' ')
node,edges=int(temp[0]),int(temp[1])
empty_dict={}
for i in range(edges):
  temp=file_in.readline().split(' ')
  first=int(temp[0])
  if first not in empty_dict.keys():
    empty_dict[first]=[(int(temp[1]),int(temp[2]))]
  else:
    empty_dict[first].append((int(temp[1]),int(temp[2])))
for i in range(node+1):
  if i not in empty_dict:
    if i!=node:
      file_out.write(f'{i}:\n')
    else:
      file_out.write(f'{i}:')
  else:
    file_out.write(f'{i}: ')
    if i!=node:
      for j in range(len(empty_dict[i])):
        if j!=(len(empty_dict[i])-1):
          file_out.write(f'{empty_dict[i][j]} ')
        else:
          file_out.write(f'{empty_dict[i][j]}\n')
    else:
      for j in range(len(empty_dict[i])):
        if j!=(len(empty_dict[i])-1):
          file_out.write(f'{empty_dict[i][j]} ')
        else:
          file_out.write(f'{empty_dict[i][j]}')
file_out.close()