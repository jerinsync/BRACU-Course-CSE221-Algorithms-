#!/usr/bin/env python
# coding: utf-8

# In[48]:


f = open('input5.txt', mode = 'r')
lines = f.readlines()
number = lines[0].strip()

outputList = []
s1 = []
s2 = []
a = number.split()
x1 = f'unsorted {number}\n'
x2 = f'a)\n'
outputList.append(x2)
outputList.append(x1)
for i in a:
    if i != ' ':
        s1 = s1 + [i]
for val in s1:
    new = int(val)
    s2 += [new]
A = s2

import time

start = time.time()

def quicksort(A, l, r, k=None):
    if l<r:
        s1=partition(A, l, r, k)
        quicksort(A, l, s1-1, k)
        quicksort(A, s1+1, r, k)

def partition(A, l, r, k=None):
    P = A[l]
    i=l
    for j in range(l+1, r+1):
        if A[j] <= P:
            i=i+1 
            A[i], A[j]=A[j], A[i]
    A[l], A[i]=A[i], A[l]
    
    if k != None:
        if r == l+1:
            if r == k:
                outputList.append(f'{k+1} position element from the sorted array {A[r]}\n')
            elif l == k:
                outputList.append(f'{k+1} position element from the sorted array {A[l]}\n')
        elif i == k:
            outputList.append(f'{k+1} position element from the sorted array {A[i]}\n')
    return i

quicksort(A,0,7)
time.sleep(1)
end = time.time()
x4 = f"time it takes to complete sorting {end - start}\n"

a1=''
for i in A:
    val = int(i)
    y = f'{val} '
    a1+=y
    
x3 = f'sorted {a1}\n'
outputList.append(x3)
outputList.append(x4)



x5 = f'b)\n'
outputList.append(x5)

elem = lines[1].strip()
dig = '0123456789'
valueOfk = ''
for j in elem:
    if j in dig:
        valueOfk += j
valueOfk = int(valueOfk)

def findk(k):
    q = quicksort(s2,0,7,k-1)
findk(valueOfk)   

f.close()    
f = open('output5.txt', mode = 'w')
f.writelines(outputList)
f.close()


# In[ ]:




