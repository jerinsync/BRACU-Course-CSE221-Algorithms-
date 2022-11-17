#!/usr/bin/env python
# coding: utf-8

# In[1]:


f = open('input2.txt', mode='r')
line = f.readlines()
z=[]
for i in line:
    i.strip()
    x = i.split()
    l2 = list(map(int,x))
    z.append(l2)

n = z[0][1]
person={}
for i in range(n):
    person[i+1]=[]

z.pop(0)
z.sort(key=lambda x:x[1])
start = []
finish = []
for i in z:
    start.append(i[0])
for i in z:
    finish.append(i[1])

count=0
for i in finish:
    person[1].append(i)
    count+=1
    break

for j in range(1,len(start)):
    for k in person.keys():
        if person[k] == []:
            person[k].append(finish[j])
            count+=1
            break
        elif start[j] >= person[k][-1]:
            person[k].append(finish[j])
            count+=1
            break
f.close()

f = open('output2.txt', mode = 'w')
f.write(f'{count}')
f.close()


# In[ ]:




