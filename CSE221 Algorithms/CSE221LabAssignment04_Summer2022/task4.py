#!/usr/bin/env python
# coding: utf-8

# In[1]:


f = open('input4.txt', mode='r')
line1 = f.readlines()
new_dict = {}
for i in range(len(line1)):
    line = line1[i]
    x = line.strip()
    z = line.split()
    cost = int(z[2])
    c1 = []
    c2 = []
    k1 = z[0]
    k2 = z[1]
    c1 += [cost, k2]
    c2 += [cost, k1]

    if k1 in new_dict.keys():
        new_dict[k1].append(c1)
    else:
        new_dict[k1] = [c1]

    if k2 in new_dict.keys():
        new_dict[k2].append(c2)
    else:
        new_dict[k2] = [c2]

import heapq
import math
p1 = []
queue = []
dist = {}
prev = {}
def Dijkstra(graph, src):
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
            if u in new_dict.keys():
                for cost, neighbour in new_dict.get(u):
                    alt = dist[u] + cost
                    if dist[neighbour] > alt and neighbour not in Sett:
                        dist[neighbour] = alt
                        prev[neighbour] = u
                        for i in queue:
                            if neighbour in i[1]:
                                queue.remove(i) 
                        heapq.heappush(queue, [alt, neighbour])
                        heapq.heapify(queue) 
                              
Dijkstra(new_dict, 'Motijheel')

def path(p, src, n, list1):
    if n == src:
        p1.append(list1)
    else:
        i = p[n]
        list1.append(i)
        path(p, src, i ,list1)
path(prev, 'Motijheel', 'MOGHBAZAR', list1=['MOGHBAZAR'])

outputList = []
x1 = f"{dist['MOGHBAZAR']}\n"
outputList.append(x1)

r = p1[0]
r.reverse()
store = ''
for i in r:
    store+=str(i)
    store+='->'
s1 = store[:-2]
x2 = f'{s1}\n'
outputList.append(x2)

f.close()


f = open('output4.txt', mode = 'w')
f.writelines(outputList)
f.close()


# In[ ]:




