#!/usr/bin/env python
# coding: utf-8

# In[2]:


f = open('input5.txt', mode='r')
line1 = f.readlines()
line1.pop(0)
outputList = []
source=[]
step=0
elem = []
connection = []
for j in range(len(line1)):
    l1 = line1[j].split()
    if len(l1) == 2:
        step+=1
        M = int(l1[1])
        if M != 0:
            new = {}
            for i in range(M):
                line = line1[step]
                x = line.strip()
                z = x.split()
                cost = int(z[2])
                c1 = []
                k1 = z[0]
                k2 = z[1]

                c1 += [cost, k2]
                if k1 in new.keys():
                    new[k1].append(c1)
                else:
                    new[k1] = [c1]
                step+=1

                if k2 not in elem:
                    elem.append(k2)
                if  k1 not in elem:
                    elem.append(k1)
            for k in elem:
                if k not in new.keys():
                    new[k] = []

            connection.append(new)
            idx = step
            src = line1[idx].strip()
            source.append(str(src))
            step+=1

        if M == 0:
            new={}
            new[l1[0]] = []
            idx = step
            src = line1[idx].strip()
            source.append(str(src))
            connection.append(new)
            step+=1
import heapq
import math
x=0
for i in connection:
    src = source[x]
    def Network(graph, src):
        dist = {}
        prev = {}
        for i in graph:
            dist[i] = float(-math.inf)
            prev[i] = None
        dist[src] = float(math.inf)
        queue = [[-dist[src], src]]
        while queue:
            m = heapq.heappop(queue)
            u = m[1]
            if u in graph.keys():
                for value, neighbour in graph.get(u):
                    val = value
                    alt = min(dist[u],val)
                    if alt > dist[neighbour]:
                        dist[neighbour] = alt
                        prev[neighbour] = u
                        heapq.heappush(queue, [-alt, neighbour])
                        heapq.heapify(queue)
        data = []
        sd = {}
        b = sorted(dist.keys())
        for key in b:
            if key not in sd.keys():
                sd[key] = dist[key]

        if sd[src] == float('inf'):
                data.append(0)
        for key in sd.keys():
            if sd[key] != float('-inf') and sd[key] != float('inf'):
                data.append(sd[key])
            if sd[key] == float('-inf'):
                data.append(-1)

        for i in data:
            if i == -1:
                data.pop(0)
                data.append(0)
                break
        outputList.append(data)

    Network(i, src)
    x+=1
    
f.close()

f = open('output5.txt', mode = 'w')
wri = []
for i in outputList:
    store = ''
    for j in i:
        store+=str(j)
        store+=' '
    x1 = f'{store}\n'
    wri.append(x1)

f.writelines(wri)
f.close()


# In[ ]:




