#!/usr/bin/env python
# coding: utf-8

# In[3]:


f = open('input4.txt', mode='r')
line = f.readlines()
import math
outputList = []
for i in line:
    c=0
    i.strip()
    x = i.split()
    x1 = list(map(int,x))
    a, b = x1[0], x1[1]
    for j in range(a,b+1):
        val = str(math.sqrt(j))
        lastdig = val[len(val)-2:]
        if val != '0.0':
            if '.0' in lastdig:
                c+=1
    outputList.append(c)
for i in outputList:
    if i == 0:
        outputList.remove(i)

f.close()

f = open('output4.txt', mode = 'w')
for i in outputList:
    f.write(f'{i}\n')
f.close()


# In[ ]:




