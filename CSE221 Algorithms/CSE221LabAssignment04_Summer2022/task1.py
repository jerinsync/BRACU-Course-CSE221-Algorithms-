#!/usr/bin/env python
# coding: utf-8

# In[2]:


f = open('input1.txt', mode='r')
line1 = f.readlines()
line1.pop(0)
outputList = []
distList = []
step=0
connection = []
for j in range(len(line1)):
    l1 = line1[j].split()
    if len(l1) == 2:
        step+=1
        N = str(l1[0])
        distList.append(N)
        M = int(l1[1])
        if M != 0:
            new = {}
            for i in range(M):
                line = line1[step]
                x = line.strip()
                z = x.split()
                cost = int(z[2])
                c1 = []
                c2 = []
                k1 = z[0]
                k2 = z[1]
                c1 += [cost, k2]
                c2 += [cost, k1]

                if k1 in new.keys():
                    new[k1].append(c1)
                else:
                    new[k1] = [c1]
                if k2 in new.keys():
                    new[k2].append(c2)
                else:
                    new[k2] = [c2]

                step+=1
            connection.append(new)
            
        if M == 0:
            new={}
            new[l1[0]] = []
            connection.append(new)

import heapq
import math
x=0
for i in connection:
    def Dijkstra(graph, src):
        dist = {}
        prev = {}
        for i in graph:
            dist[i] = float(math.inf)
            prev[i] = None
        dist[src] = 0
        Sett = set()
        queue = [[0, src]]
        while queue:
            m = heapq.heappop(queue)
            u = m[1]
            if u not in Sett:
                Sett.add(u)
                if u in graph.keys():
                    for value, neighbour in graph.get(u):
                        alt = dist[u] + value   
                        if dist[neighbour] > alt and neighbour not in Sett:
                            dist[neighbour] = alt
                            prev[neighbour] = u
                            for i in queue:
                                if neighbour in i[1]:
                                    queue.remove(i) 
                            heapq.heappush(queue, [alt, neighbour])
                            heapq.heapify(queue)
        t = distList[x]          
        x2 = f'{dist[t]}\n'
        outputList.append(x2)
       
    Dijkstra(i, '1')
    x+=1

f.close()
f = open('output1.txt', mode = 'w')
f.writelines(outputList)
f.close()


# In[ ]:




