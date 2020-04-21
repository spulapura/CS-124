from collections import deque

n,m = map(int, raw_input().split())
graph = {}
edges = []
for i in range(0, m):
	a,b,c,d = map(int, raw_input().split())
	edges.append((a,b,c,d))
tsa = map(int, raw_input().split())
for edge in edges:
	a, b, c = edge[0], edge[1], edge[2]*edge[3]
	if a+n not in graph:
		graph[a+n] = {b: c, a: 0}
	else:
		graph[a+n][b] = c
		graph[a+n][a] = 0
	if b+n not in graph:
		graph[b+n] = {b: 0}
	else:
		graph[b+n][b] = 0
	if a not in graph:
		graph[a] = {a+n: tsa[a-1]}
	else:
		graph[a][a+n] = tsa[a-1]
	if b not in graph:
		graph[b] = {b+n: tsa[b-1], a+n: 0}
	else:
		graph[b][b+n] = tsa[b-1]
		graph[b][a+n] = 0

#print graph

def bfs(graph):
	queue = deque([1])
	dist = [float("inf")]*(2*n+2)
	prev = [None]*(2*n+2)
	visited = [False]*(2*n+2)
	dist[1] = 0
	visited[1] = True
	while queue:
		u = queue.popleft()
		if u in [2+n,3+n,4+n]:
			return u, prev
		for v in graph[u].keys():
			if not visited[v]:
				if graph[u][v] > 0:
					queue.append(v)
					dist[v] = dist[u]+1
					visited[v] = True
					prev[v] = u
	return None, None



def maxflow(graph):
	keys = graph.keys()
	flow = 0

	while True:
		u, prev = bfs(graph)
		sink = u
		if u == None:
			return flow
		else:
			v = prev[u]
			augpath = float('inf')
			while u != 1:
				augpath = min(augpath, graph[v][u])
				u = v
				v = prev[u]
			flow += augpath
			u = sink

			while u != 1:
				v = prev[u]
				graph[u][v] += augpath
				graph[v][u] -= augpath
				u = v 


print maxflow(graph)



				







