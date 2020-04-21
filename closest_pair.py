from collections import deque
import random


#n,m,k = map(int, raw_input().split())
graph = {}
edges = []

ri = 50

edges = [(random.randint(1,ri), random.randint(1,ri)) for i in range(100)]
for i in edges:
	if i[0] in graph:
		graph[i[0]].append(i[1])
	else:
		graph[i[0]] = [i[1]]
	if i[1] in graph:
		graph[i[1]].append(i[0])
	else:
		graph[i[1]] = [i[0]]

vacant = random.sample(graph.keys(), 5)
vacant.sort()
n = ri
m = len(edges)
k = len(vacant)


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


print least_dist(vacant, vacant, n)

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





def bfs3(vacant, n):
	queue = deque(vacant)
	dist = [float("inf")]*(n+1)
	visited = [False]*(n+1)
	nearest_k = {}
	for v in vacant:
		nearest_k[v] = [v]
		visited[v] = True
		dist[v] =0
	while queue:
		b = queue.popleft()
		for i in graph[b]:
			if not visited[i]:
				if bool_vacant[b]:
					nearest_k[i] = [b]
				else:
					nearest_k[i] = nearest_k[b]
				queue.append(i)
				dist[i] = dist[b] +1
				visited[i] = True
			else:
				if bool_vacant[b]:
					nearest_k[i].append(b)
				elif dist[i] == dist[b]+1:
					nearest_k[i] = merge(nearest_k[i], nearest_k[b])

	return dist, nearest_k


#print dist, nearest_k


mindist = float('inf')
minA=float('inf')
minB = float('inf')

#print dist

def listmin(list1, list2):
	len1 = len(list1)
	len2 = len(list2)
	if list1[0] != list2[0]:
		min1, min2 = list1[0], list2[0]
	elif len1 == 1 and len2 == 1:
		min1, min2 = list1[0], list2[0]
	elif len1 == 1 and len2 > 1:
		min1 = list1[0]	
		min2 = list2[1]
	elif len1 > 1 and len2 == 1:
		min2 =list2[0]
		min1 = list1[1]
	elif list1[1] < list2[1]:
		min1 = list1[1]
		min2 = list2[0]
	else:
		min1 = list1[0]
		min2 = list1[1]

	return min(min1, min2), max(min1, min2)

		
"""

for edge in edges:
	a = edge[0]
	b = edge[1]
	if a not in nearest_k or b not in nearest_k:
		continue
	a_min, b_min = listmin(nearest_k[a], nearest_k[b])
	print edge, a_min, b_min, dist[a]+dist[b]
	#print edge, a_min, b_min

	if a_min != b_min:
		if dist[a] + dist[b] < mindist:
			minA = a_min
			minB = b_min
			mindist = dist[a] + dist[b]
			print edge, True, mindist
		elif dist[a] + dist[b] == mindist:
			if a_min < minA:
				minA = a_min
				minB = b_min
				mindist = dist[a] + dist[b]
				print edge, True, mindist
			elif a_min == minA:
				if b_min< minB:
					minA= a_min
					minB = b_min
					mindist = dist[a] + dist[b]
					print edge, True, mindist

"""

def bfs2(vacant, n):
	queue = deque(vacant)
	dist = [float("inf")]*(n+1)
	visited_by = {}
	shortest_paths = []
	dist= [float('inf')]*(n+1)
	min_dist = float('inf')
	for v in vacant:
		visited_by[v] = [v]
		dist[v] = 0
	while queue:
		b = queue.popleft()
		if dist[b] > min_dist and len(shortest_paths)>0:
			return shortest_paths
		for i in graph[b]:
			if i not in visited_by:
				visited_by[i] = visited_by[b]
				queue.append(i)
				dist[i] = dist[b]+1
			else:
				visited_by[i] = merge(visited_by[i], visited_by[b])
			if len(visited_by[i]) >=2:
				shortest_paths.append(visited_by[i])
				min_dist = dist[b]



shortest_pairs = bfs2(vacant, n)
print shortest_pairs
#print str(a) + " " + str(b) 