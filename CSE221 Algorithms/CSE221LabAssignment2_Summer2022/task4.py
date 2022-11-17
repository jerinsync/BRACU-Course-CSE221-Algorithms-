#!/usr/bin/env python
# coding: utf-8

# In[5]:


f = open('input4.txt', mode='r')
lines = f.readlines()
elements = lines[1].strip()
s1 = []
s2 = []
a = elements.split()
for i in a:
    if i != ' ':
        s1 = s1 + [i]
for val in s1:
    new = int(val)
    s2 += [new]
myList = s2

def merge(L, R): 
    n1 = len(L)
    n2 = len(R)

    C = []
    i=0
    j=0
    while i<n1 and j<n2:
        if (L[i] <= R[j]):
            C = C + [L[i]]
            i += 1
        else:
            C = C + [R[j]]
            j += 1

    if i >= n1:
        rem = R[j:]
        C = C + rem
        
    if j >= n2:
        rem = L[i:]
        C = C + rem
        
    return C

def mergesort(A):
    if len(A) == 1:
        return A
    else:
        length = len(A)
        div=length//2
        A1 = mergesort(A[:div])
        A2 = mergesort(A[div:])
        return merge(A1,A2)

n = len(myList)
s3 = mergesort(myList)
f.close()

f = open('output4.txt', mode = 'w')
for i in s3:
    num = str(i)
    f.write(f'{num} ')

f.close()


# In[ ]:




