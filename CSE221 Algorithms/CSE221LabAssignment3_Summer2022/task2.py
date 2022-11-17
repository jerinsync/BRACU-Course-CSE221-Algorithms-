#!/usr/bin/env python
# coding: utf-8

# In[1]:


f = open('task2.txt', mode = 'r')
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
queue = []
outputList = []
def BFS(visited, graph, node, endPoint):
    visited[int(node) - 1] = 1
    queue.append(node)
    while queue:
        m = queue.pop(0)
        t1 = f'{m}'
        outputList.append(t1)
        if(m == endPoint):
            break
        if m in dictionary.keys():
            for neighbour in graph[m]:
                if(visited[int(neighbour) - 1] == 0):
                    visited[int(neighbour) - 1] = 1
                    queue.append(neighbour)

BFS(visited, dictionary, 1, 12)
f.close()

f = open('output2.txt', mode = 'w')
for i in outputList:
    f.write(f'{i} ')
f.close()


# In[ ]:




