#!/usr/bin/env python
# coding: utf-8

# In[1]:


f = open('task1.txt', mode = 'r')
lines = f.read().strip().split('\n')
lines.pop(0)
lines.pop(0)
dictionary = {}
for i in lines:
    a = i.split()
    s1 = int(a[0])
    s2 = int(a[1])
    c1 = []
    c1 = c1 + [s2]
    if s1 in dictionary.keys():
        dictionary[s1].append(s2)
    else:
        dictionary[s1] = c1

c2=[]
for j in dictionary:
    x = dictionary[j]
    for i in x:
        if i not in c2:
            c2 += [i]
            
for k in c2:
    if k not in dictionary.keys():
        dictionary[k] = []
f.close()

outputList = []
t1 = f'{dictionary}\n'
outputList.append(t1)

f = open('output1.txt', mode = 'w')
for k, v in dictionary.items():
    e1 = ''
    for i in v:
        e1 += str(i) 
        e1 += ','
    e1 = e1[:-1]
    t2 = f'{k} ---> {e1}\n'
    outputList.append(t2)

f.writelines(outputList)
f.close()
    


# In[ ]:




