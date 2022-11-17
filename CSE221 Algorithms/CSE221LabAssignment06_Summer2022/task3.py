#!/usr/bin/env python
# coding: utf-8

# In[4]:


f = open('input3.txt', mode='r')
line = f.readlines()
x = line[0].strip()
y = line[1].strip()
z = line[2].strip()

def LCS(x, y, z):
    m = len(x)
    n = len(y)
    o = len(z)
    c=[]

    for i in range(m+1):
       c.append([])
       for j in range(n+1):
           c[i].append([])
           for k in range(o+1):
               c[i][j].append([])

    for i in range(m+1):
       for j in range(n+1):
         for k in range(o+1):
            if i == 0 or j == 0 or k == 0:
                c[i][j][k] = 0

            else:
                if x[i-1] == y[j-1] and x[i-1] == z[k-1]:
                    c[i][j][k] = 1 + c[i-1][j-1][k-1]

                else:
                    if c[i-1][j][k] >= c[i][j-1][k]:
                        max = c[i-1][j][k]
                        if max >= c[i][j][k-1]:
                            c[i][j][k] = max

                        else:
                            max = c[i][j][k-1]
                            c[i][j][k] = max

                    else:
                        max = c[i][j-1][k]
                        if max >= c[i][j][k-1]:
                            c[i][j][k] = max
                                                    
                        else:
                            max = c[i][j][k-1]
                            c[i][j][k] = max

    lcs=c[-1][-1][-1]
    f = open('output3.txt', mode = 'w')
    f.write(f'{lcs}')
    f.close()

LCS(x, y, z)
f.close()


# In[ ]:




