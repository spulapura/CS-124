import heapq

n,m,k = map(int, raw_input().split())
edges=[]
count=0
graph ={}

for i in range(0,m):
	a,b,c = map(int, raw_input().split())
	if a in graph:
		graph[a].append((c,b))
	else:
		graph[a] = [(c,b)]
	if b in graph:
		graph[b].append((c,a))
	else:
		graph[b] = [(c,a)]
	count+= c

for i in range(0,k):
	a,b,c = map(int, raw_input().split())
	if a in graph:
		graph[a].append((c,b))
	else:
		graph[a] = [(c,b)]
	if b in graph:
		graph[b].append((c,a))
	else:
		graph[b] = [(c,a)]


#print graph

def mst(start):
	s = set([])
	h = []
	heapq.heapify(h)
	white_count = 0
	heapq.heappush(h, (0,start))
	while len(h) >0:
		v=heapq.heappop(h)
		v_weight = v[0]
		v_start = v[1]
		#print s
		#print v_start
		if v_start not in s:
			#print True
			s.add(v_start)
			white_count+=v_weight
			#print white_count
			for n in graph[v_start]:
				heapq.heappush(h, n)
	return white_count


white_count = mst(graph.keys()[0])

print count-white_count


