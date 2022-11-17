#!/usr/bin/env python
# coding: utf-8

# In[2]:


f = open('input3.txt', mode='r')
line = f.readlines()
line.pop(0)
outputList = []
for i in line:
    x = i.strip()
    y1 = x.split()
    break
line.pop(0)
q1 = sorted(list(map(int,y1)))
for i in line:
    x = i.strip()
    
jack = 0
jill = 0
taskjill = []
total = ''
for k in x:
    if k =='J':
        total += str(q1[0])
        jack+=q1[0]
        taskjill.append(q1[0])
        q1.pop(0)
    if k =='j':
        h = taskjill[-1]
        total += str(h)
        jill += h
        taskjill.pop(-1)

outputList.append(total)
outputList.append(f'Jack will work for {jack} hours')
outputList.append(f'Jill will work for {jill} hours')

f.close()
f = open('output3.txt', mode = 'w')
for i in outputList:
    f.write(f'{i}\n')
f.close()


# In[ ]:




