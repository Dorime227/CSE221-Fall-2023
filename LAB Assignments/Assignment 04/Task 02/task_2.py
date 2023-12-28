# -*- coding: utf-8 -*-
"""Task 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ysf89-b7-MPYQ4HrZ3XnDP9cf4QymiMO
"""

file_in=open('input2.txt','r')
file_out=open('output2.txt','w')
temp=file_in.readline().split(' ')
node,edges=int(temp[0]),int(temp[1])
ad_list=[[] for i in range(node+1)]
visited_list=[0 for i in range(node+1)]
for i in range(1,edges+1):
  temp=file_in.readline().split(' ')
  ad_list[int(temp[0])].append(int(temp[1]))
def BFS(ad_list,source):
  visited_list[source]=1
  queue=[]
  queue.append(source)
  while len(queue)!=0:
    temp=queue.pop(0)
    file_out.write(f'{temp} ')
    for j in ad_list[temp]:
      if visited_list[j]==0:
        visited_list[j]=1
        queue.append(j)

source=1
BFS(ad_list,source)
file_out.close()