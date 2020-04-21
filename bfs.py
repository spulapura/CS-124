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
vacant.sort()
#print vacant

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


dist, nearest_k = bfs2(vacant, n)


#print dist, nearest_k


mindist = float('inf')
minA=float('inf')
minB = float('inf')

#print dist

def listmin(list1, list2, dist1, dist2):
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







for edge in edges:
	a = edge[0]
	b = edge[1]
	a_min, b_min = listmin(nearest_k[a], nearest_k[b], dist[a], dist[b])
	#print edge, a_min, b_min, nearest_k[a], nearest_k[b]

	if a_min != b_min:
		if dist[a] + dist[b] +1 < mindist:
			minA = a_min
			minB = b_min
			mindist = dist[a] + dist[b]+1
			#print edge, True, minA, minB
		elif dist[a] + dist[b]+1 == mindist:
			if a_min < minA:
				minA = a_min
				minB = b_min
				mindist = dist[a] + dist[b]+1
				#print edge, True, minA, minB
			elif a_min == minA:
				if b_min< minB:
					minA= a_min
					minB = b_min
					mindist = dist[a] + dist[b]+1
					#print edge, True, minA, minB





print str(minA) + " " + str(minB)

