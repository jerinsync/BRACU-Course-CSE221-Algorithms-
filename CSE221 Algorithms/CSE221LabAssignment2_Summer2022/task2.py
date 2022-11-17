#!/usr/bin/env python
# coding: utf-8

# In[7]:


f = open('input2.txt', mode = 'r')
lines = f.readlines()
b = lines[0]
c = []
for i in b:
    if i != ' ':
        c = c + [i]

num = c[-2]
num = int(num)
a = lines[1].strip()
s1 = []
s2 = []
a = a.split()

for i in a:
    if i != ' ':
        s1 = s1 + [i]

for val in s1:
    new = int(val)
    s2 = s2 + [new]
    f = open('input2.txt', mode='r')

for i in range(len(s2)):
    index = i
    for j in range(i+1, len(s2)):
        if s2[index] > s2[j]:
            index = j
    s2[i], s2[index] = s2[index], s2[i]

s4 = s2[:num]
f.close()
f = open('output2.txt', mode='w')
s3 = []
for i in s4:
    val = str(i)
    s3 = s3 + [val]
    f.write(f'{val} ')

print(s3)

f.close()


# In[ ]:




