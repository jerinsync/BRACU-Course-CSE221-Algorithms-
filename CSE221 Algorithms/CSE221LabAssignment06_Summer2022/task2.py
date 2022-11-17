#!/usr/bin/env python
# coding: utf-8

# In[1]:


f = open('input2.txt', mode='r')
line = f.readlines()
numberOfZones = int(line[0].strip())
X = line[1].strip()
Y = line[2].strip()

zone = {'Y': 'Yasnaya', 'P': 'Pochinki', 'S': 'School', 'R': 'Rozhok', 'F': 'Farm', 'M': 'Mylta', 'H': 'Shelter', 'I': 'Prison'}
def LCS(X, Y):
    outputList=[]
    m = len(X)
    n = len(Y)
    
    c=[]
    for i in range(m+1):
        temp=[]
        for j in range(n+1):
            temp.append(0)
        c.append(temp)
    
    t=[]
    for i in range(m+1):
        temp=[]
        for j in range(n+1):
            temp.append(None)
        t.append(temp)

    for i in range(1,m+1):
        for j in range(1,n+1):
            if (X[i-1] == Y[j-1]):
                c[i][j] = c[i - 1][j - 1] + 1
                t[i][j] = 'D'
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                t[i][j] = 'U'
            else:
                c[i][j] = c[i][j-1]
                t[i][j] = 'L'

    leng = c[m][n]
    correctness = f'Correctness of prediction: {(leng*100)//numberOfZones}%'
    lcs=[]
    i=m
    j=n
    while i > 0 and j> 0:
        if X[i-1] == Y[j-1]:
            lcs += X[i-1]
            i-=1
            j-=1
        elif c[i-1][j]>c[i][j-1]:
            i-=1
        else:
            j-=1
    lcs.reverse()
    l1=''
    for i in lcs:
        l1 += zone[i]
        l1 += ' '
        
    outputList.append(l1)
    outputList.append(correctness)
    f = open('output2.txt', mode = 'w')
    for i in outputList:
        f.write(f'{i}\n')
    f.close()

LCS(X, Y)
f.close()


# In[ ]:




