#!/usr/bin/env python
# coding: utf-8

# In[2]:


f = open('task4.txt', mode = 'r')
lines = f.read().split('\n')
lines.pop(0)
value = lines[0].split()
M = int(value[-1])
lines.pop(0)
graph = []
graphList = []
x=0

for k in range(len(lines)):
    graph = []
    for i in range(x,M):
        graph += [lines[i]]
    l1 = len(graph)
    for i in range(l1):
        lines.pop(0)
    graphList += [graph]
    if len(lines) == 0:
        break
    value = lines[x].split()
    lines.pop(0)
    M = int(value[-1])

outputList=[]
for graph in graphList:
    dictionary = {}
    for i in graph:
        a = i.split()
        s1 = int(a[0])
        s2 = int(a[1])
        c1 = []
        c1 = c1 + [s2]
        c2 = []
        c2 = c2 + [s1]
        if s1 in dictionary.keys():
            dictionary[s1].append(s2)
        else:
            dictionary[s1] = c1

        if s2 in dictionary.keys():
            dictionary[s2].append(s1)
        else:
            dictionary[s2] = c2

    queue = []
    dis = {}
    color = {}
    parent = {}
    allNodes = []
    for n in dictionary.items():
        allNodes.append(n[0])
    source = allNodes[0]
    end = allNodes[-1]

    def BFS(graph, node, endPoint):
        for i in graph:
            color[i] = 'White'
            dis[i] = -1
            parent[i] = []
        color[node] = 'Gray'
        dis[node] = 0
        parent[node].append(None)
        queue.append(node)
        while queue:
            m = queue.pop(0)
            if m in dictionary.keys():
                for neighbour in graph[m]:
                    if color[neighbour] == 'White':
                        color[neighbour] = 'Gray'
                        dis[neighbour] = dis[m]+1
                        parent[neighbour].append(m)
                        queue.append(neighbour)
                        
                    elif color[neighbour] == 'Gray':
                        if parent[m] != neighbour or parent[neighbour] != m:
                            parent[neighbour].append(m)
                        
                color[m] = 'Black'
    BFS(dictionary, source, end)


    numberOfWays = []
    def path(graph, source, n, list1):
        if n==source:
            numberOfWays.append(len(list1))
            list1 = list1.clear()
        else:
            for i in range(len(parent[n])):
                list1.append(parent[n][i])
                path(graph, source, parent[n][i], list1)

    path(dictionary, source, end, list1=[])



    data = min(numberOfWays)
    t1 = f'{data}\n'
    outputList.append(t1)
    
f.close()
     
f = open('output4.txt', mode = 'w')
for i in outputList:
    f.write(f'{i}')
f.close()


# In[ ]:




