# -*- coding: utf-8 -*-
"""task4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19C9VUhlC9KbygghfVLsJAeQkT9gZsZo5
"""

file_in=open('input4.txt','r')
file_out=open('output4.txt','w')
temp=file_in.readline().split(' ')
total_case,total_workers=int(temp[0]),int(temp[1])
list1=[0]*total_case

#creating a list from the input
for i in range(total_case):
  temp=file_in.readline().split(' ')
  if i!=total_case-1:
    list1[i]=tuple((int(temp[0]),int(temp[-1][:-1])))
  else:
    list1[i]=tuple((int(temp[0]),int(temp[-1][0:])))

#sorting the list by the end time
for i in range(len(list1)):
  min_idx=i
  for j in range(i+1,len(list1)):
    if list1[min_idx][-1]>list1[j][-1]:
      min_idx=j
  list1[i], list1[min_idx]= list1[min_idx],list1[i]
work_hour=[0]*total_workers #for storing the end time
total_works=[] #for storing the work times

for i in range(len(list1)):
  min=9999999999999999999999999999999999 #for minimum difference check
  available_counter=0 #checking number of available workers,if it's >1 then it will be add in the total work list
  for j in range(len(work_hour)):
    if work_hour[j]<=list1[i][0]: #checking if ending time of current works <= the current work
      diff=list1[i][0]-work_hour[j]
      if diff==0: #who have the time difference 0 will get the work instantly
        work_hour[j]=list1[i][-1]
        total_works.append(list1[i])
        available_counter=0
        break
      elif min>diff: #if not then chceking who's time difference is minimum
        available_counter+=1
        min=diff
        min_idx=j

  if available_counter>0: #checking if available workers>0 if yes then the work time add on the total_works list
    work_hour[min_idx]=list1[i][-1] #updating the ending time via minimum difference indexing
    total_works.append(list1[i])
file_out.write(f'{len(total_works)}')
file_out.close()