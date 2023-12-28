# -*- coding: utf-8 -*-
"""Task01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TiiQJdcwEFqPqlRpW5LjZWCquNcU2qlQ
"""

def merge(list1, list2):
    pointer1=0
    pointer2=0
    pointer3=0
    new_list=[0]*(len(list1)+len(list2))
    while pointer1<len(list1) or pointer2<len(list2):
      if pointer1==len(list1):
        new_list[pointer3:]=list2[pointer2:]
        break
      elif pointer2==len(list2):
        new_list[pointer3:]=list1[pointer1:]
        break
      elif list1[pointer1]<list2[pointer2]:
        new_list[pointer3]=list1[pointer1]
        pointer1+=1
        pointer3+=1
      elif list1[pointer1]==list2[pointer2]:
        new_list[pointer3]=list1[pointer1]
        pointer3+=1
        new_list[pointer3]=list2[pointer2]
        pointer1+=1
        pointer2+=1
        pointer3+=1
      else:
        new_list[pointer3]=list2[pointer2]
        pointer2+=1
        pointer3+=1
    return new_list
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[:mid])  # write the parameter
        a2 = mergeSort(arr[mid:])  # write the parameter
        return merge(a1, a2)

file_in=open('input1.txt','r')
file_out=open('output1.txt','w')
test_case=int(file_in.readline())
list1=list(map(int,file_in.readline().split(' ')))
output=mergeSort(list1)
for i in range(len(output)):
  if i!=len(list1)-1:
    file_out.write(f'{output[i]} ')
  else:
    file_out.write(f'{output[i]}')
file_out.close()