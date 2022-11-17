#!/usr/bin/env python
# coding: utf-8

# In[2]:


f = open('input1.txt',mode = 'r')
lines = f.readlines()
a = lines[1].strip()
s1 = []
s2 = []
for i in a:
    if i != ' ':
        s1 = s1 + [i]
for val in s1:
    new = int(val)
    s2 = s2 + [new]

def bubbleSort(arr):
    for i in range(len(arr)-1):
        flag = 0
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                flag+=1
        if flag == 0:
            break
#A counter is used to keep track if the adjacent number was swapped while comparing two numbers in the bubble sort. 
#the counter will be 0 if the adjacent elements are not swapped in the inner loop, indicating the array has already been sorted. 
#Despite the array being sorted normally in bubble sort, the first loop iterates through the array. 
#So altering the code by using 'break' statement there will be no need for the first loop to traverse over the array again. 
#Therefore, in the best-case scenario, complexity is O(n) when the array has already been sorted.
bubbleSort(s2)
f.close()
f = open('output1.txt', mode = 'w')
for i in s2:
    val = str(i)
    f.write(f'{val} ')

f.close()


# In[ ]:




