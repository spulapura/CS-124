import random
from collections import deque

n,m,k = map(int, raw_input().split())
graph ={}
edges = []

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

bool_vacant = [False]*(n+1)

for v in vacant:
	bool_vacant[v] = True



def merge(s, t):
  s_len = len(s)
  t_len = len(t)
  n = s_len + t_len
  v =[]
  p = 0
  q = 0
  while(p<s_len and q<t_len):
    if t[q] < s[p]:
      v.append(t[q])
      q+=1
    elif t[q]>s[p]:
      v.append(s[p])
      p+=1
    else:
    	v.append(t[q])
    	q+=1
    	p+=1
  while(p<s_len):
    v.append(s[p])
    p+=1
  while(q<t_len):
    v.append(t[q])
    q+=1
  return v





def bfs2(vacant, n):
	queue = deque(vacant)
	dist = [float("inf")]*(n+1)
	visited_by = {}
	shortest_paths = []
	for v in vacant:
		visited_by[v] = [v]
	while queue:
		b = queue.popleft()
		for i in graph[b]:
			if i not in visited_by:
				visited_by[i] = visited_by[b]
				queue.append(i)
			else:
				visited_by[i] = merge(visited_by[i], visited_by[b])
			if len(visited_by[i]) >=2:
				return visited_by[i]


a, b = bfs2(vacant, n)
print str(a) + " " + str(b) 




def dp(sccs,b):
	store1 = [-float('inf')]*(b+1)
	store2 = [-float('inf')]*(b+1)
	for scc in range(0, len(sccs)):
		for i in range(0, len(sccs[scc])):
			for j in range(i+1, len(sccs[scc])):
				item1 = sccs[scc][i]
				item2 = sccs[scc][j]
				cost = servers[item1][0]+servers[item2][0]
				if cost<= b:
					value = servers[item1][1] + servers[item2][1]
					if value>= store1[cost]:
						store1[cost] = value
		if scc==0:
			store2 = [item for item in store1]
			store1 = [-float('inf')]*(b+1) 	
			continue			
		for i in range(0, len(store1)):
			for j in range(0, len(store2)):
				if i+j <= b:
					if store1[i] + store2[j] > store2[i+j]:
						store2[i+j] = store1[i] + store2[j]
		store1 = [-float('inf')]*(b+1)
	return store2[b]


