#!/usr/bin/env python
# coding: utf-8

# In[3]:


f = open('input3.txt', mode = 'r')
lines = f.readlines()
ID = lines[1].strip()
num = lines[2].strip()
s1 = []
s2 = []
a = ID.split()
for i in a:
    if i != ' ':
        s1 = s1 + [i]
for val in s1:
    new = int(val)
    s2 += [new]
    
ID = s2

s3=[]
s4=[]
b = num.split()
for i in b:
    if i != ' ':
        s3+=[i]
for val in s3:
    new = int(val)
    s4 += [new]

Marks = s4

def insertionSort(Marks,ID):
    for i in range(1, len(Marks)):
        key = Marks[i]
        k = ID[i]
        j = i-1
        while j >= 0 and key > Marks[j]:
            Marks[j+1] = Marks[j]
            ID[j+1] = ID[j]
            j-=1
        Marks[j+1] = key
        ID[j+1] = k

insertionSort(Marks,ID)
f.close()

f = open('output3.txt', mode = 'w')
for i in ID:
    f.write(f'{i} ')
f.close()


# In[ ]:




