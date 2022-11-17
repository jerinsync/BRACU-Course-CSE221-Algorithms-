#!/usr/bin/env python
# coding: utf-8

# In[4]:


f = open('input1.txt', mode='r')
line = f.readlines()
line.pop(0)
z=[]
outputList=[]
for i in line:
    i.strip()
    x = i.split()
    l1 = list(map(int,x))
    z.append(l1)
c=0
z.sort(key=lambda x: x[1])

p1 = []
for i in z:
    p1.append(i)
    finish = i[1]
    c+=1
    break

for j in range(1,len(z)):
    if z[j][0] >= finish:
        finish = z[j][1]
        p1.append(z[j])
        c+=1

outputList.append(str(c))
for i in p1:
    a, b = i[0], i[1]
    stg = ''
    stg+=str(a)
    stg+=' '
    stg+=str(b)
    outputList.append(stg)
    
f.close()
f = open('output1.txt', mode = 'w')
for i in outputList:
    f.write(f'{i}\n')
f.close()


# In[ ]:




