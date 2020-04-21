graph = {}
edges = []

import random
from collections import deque

"""

edges = [(random.randint(1,50), random.randint(1,50)) for i in range(100)]
for i in edges:
	if i[0] in graph:
		graph[i[0]].append(i[1])
	else:
		graph[i[0]] = [i[1]]
	if i[1] in graph:
		graph[i[1]].append(i[0])
	else:
		graph[i[1]] = [i[0]]

vacant = random.sample(graph.keys(), 2)
vacant.sort()
n = len(graph.keys())
m = len(edges)
k = len(vacant)
"""

n,m,k = map(int, raw_input().split())

for i in range(0,m):
	a,b = map(int, raw_input().split())
	if a in graph:
		graph[a].append(b)
	else:
		graph[a] = [b]
	if b in graph:
		graph[b].append(a)
	else:
		graph[b] = [a]
	edges.append((a,b))

vacant = map(int, raw_input().split())

d = [[float("inf") for i in range(0, n+1)] for j in range(0, n+1)]


for edge in edges:
	x_val = edge[0]
	y_val = edge[1]
	d[x_val][y_val] = 1
	d[y_val][x_val] = 1

for i in range(0, len(d)):
	d[i][i] = 0

current_min = float("inf")
#print vacant

for x in range(0, n+1):
	for y in vacant:
		for z in vacant:
			d[y][z] = min(d[y][z], d[y][x]+ d[x][z])
			if d[y][z] < current_min and y!=z:
				current_min = d[y][z]
				current_a = y
				current_b = z




def bfs(a, n, b=None, steps=float("inf")):
	if(a==b):
		return float("inf")
	queue = deque([a])
	dist = {}
	dist[a] = 0
	visited = {}
	visited[a] = True
	while queue:
		nex = queue.popleft()
		if b == nex:
			return dist[b]
		if dist[nex] < steps:
			for i in graph[nex]:
				if i not in visited:
					queue.append(i)
					dist[i] = dist[nex]+1
					visited[i] = True
	return dist 




def least_dist(left, right, n):
	mindist = float("inf")
	maxA = 0
	maxB = 0
	for i_index in range(0, len(left)):
		for j_index in range(0, len(right)):
			i = left[i_index]
			j = right[j_index]
			dist = bfs(i,n, j) 
			if i != j:
				if dist < mindist:
					maxA = i
					maxB = j
					mindist = dist
				elif dist == mindist:
					if i < maxA:
						maxA = i
						maxB = j
						mindist = dist
					elif i == maxA:
						if j < maxB:
							maxA = i 
							maxB = j
							mindist = dist
	if(maxA > maxB):
		return maxB, maxA, mindist
	else:
		return maxA, maxB, mindist


print str(current_a) + " " + str(current_b)
#print least_dist(vacant, vacant, n)

