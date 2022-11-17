#!/usr/bin/env python
# coding: utf-8

# In[3]:


f = open('task3.txt', mode = 'r')
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
        

visited = [0] * 12
printed = []
endPoint = 12
outputList=[]

def DFS_VISIT(graph, node):
    visited[int(node) - 1] = 1
    printed.append(node)
    if node in dictionary.keys():
        for i in graph[node]:
            if(i not in visited):
                DFS_VISIT(graph, i)


def DFS(graph, endPoint):
    for m in graph:
        if(m not in visited):
            DFS_VISIT(graph, m)
            
    for n in printed:
        t1 = f'{n}'
        outputList.append(t1)
        if(n == endPoint):
            break
    
DFS(dictionary, 12)
f.close()

f = open('output3.txt', mode = 'w')
for i in outputList:
    f.write(f'{i} ')
f.close()


# In[ ]:




