from collections import deque
import sys
sys.setrecursionlimit(20000000)


n,m,b = map(int, raw_input().split())
servers =[None]*(n+1)
graph=  {}

for i in range(0, m):
	x, y = map(int, raw_input().split())
	if x in graph:
		graph[x].append(y)
	else:
		graph[x] = [y]
	if y not in graph:
		graph[y] = []
for i in range(1, n+1):
	x,y = map(int, raw_input().split())
	servers[i] = (x,y)


keys = graph.keys()


def search(g, v, scc, visited, post):
	scc.append(v)
	visited[v] = True
	for w in g[v]:
		if not visited[w]:
			search(g, w, scc, visited, post)
	post.append(v)
	return scc, visited, post

def dfs(g, keys, scc, all_sccs):
	count =0
	visited = [False]*(n+1)
	post = []
	for v in keys:
		if not visited[v]:
			count +=1
			scc, visited, post = search(g, v, scc, visited, post)
			all_sccs.append(scc)
			scc = []
	return post, all_sccs, count

ms = dfs(graph, keys, [], [])[0][-1]
len_ms = len(search(graph, ms, [], [False]*(n+1), [])[0])

if len_ms == n:
	ms_exists = True
else:
	ms_exists = False



def invert(graph):
	inv = {}
	for k in graph.keys():
		for v in graph[k]:
			if v in inv:
				inv[v].append(k)
			else:
				inv[v] = [k]
		if k not in inv:
			inv[k] = []
	return inv

def kosaraju(graph):
	inv = invert(graph)
	post = dfs(inv, inv.keys(), [], [])[0]
	post.reverse()
	return dfs(graph, post, [],[])[1]

scc_indices = [None]*(n+1)	

sccs = kosaraju(graph)
postorder_list = deque([])
for i in range(0, len(sccs)):
	for j in sccs[i]:
		scc_indices[j] = i
		postorder_list.appendleft(j)
postorder_list.appendleft(0)

#print postorder_list
#print scc_indices

def X(k, b):
	#print(k,b)
	if(k==0 and b>=0):
		return 0
	elif(b<0):
		return -float('inf')
	else:
		return max(X(k-1,b), X(k-1, b-servers[k][0])+servers[k][1])

def find(i, b, scc_num, scc_val, index, sccs):
	k = postorder_list[i]
	if(k==0 and b>= 0 and scc_val==2):
		return 0
	elif(b<0):
		return -float('inf')
	elif(scc_val > 2):
		return -float('inf')
	elif(k==0 and scc_val<2):
		return -float('inf')
	else:
		if index == len(sccs[scc_num]):
			if(scc_val != 2):
				return -float('inf')
			else:
				index = 0
				scc_num +=1
				scc_val = 0
		return max(find(i-1, b, scc_num, scc_val, index+1, sccs), find(i-1, b-servers[k][0], scc_num, scc_val+1, index+1, sccs) + servers[k][1])



def dp(b, sccs):
	array = [[0]*(b+1),[-float('inf')]*(b+1),[-float('inf')]*(b+1)] 
	array_prev = [[0]*(b+1),[-float('inf')]*(b+1),[-float('inf')]*(b+1)]
	for scc in sccs:
		for item in scc:
			for cost in range(0, b+1):
				for serv in range(0,3):
					val = servers[item][0]
					if val > cost:
						array[serv][cost] = array_prev[serv][cost]
					elif serv == 0:
						array[serv][cost] = array_prev[serv][cost]
					else:
						#print array_prev[serv-1][cost-val], serv, cost
						array[serv][cost] = max(array_prev[serv][cost], array_prev[serv-1][cost-val]+servers[item][1])
			array_prev = [list(i) for i in array]
			array = [list(array_prev[0]),[-float('inf')]*(b+1),[-float('inf')]*(b+1)]
		array_prev = [list(array_prev[2]), [-float('inf')]*(b+1), [-float('inf')]*(b+1)]
		array = [list(i) for i in array_prev]
	return array_prev[0][b]





def test(b,n):
	for scc in sccs:
		if len(scc) <2:
			return 'Impossible'
	if ms_exists == False:
		return 'Impossible'
	if b==n:
		return len(sccs)*2
	else:
		v = dp(b,sccs)
		if v == -float('inf'):
			return 'Impossible'
		else:
			return v


print test(b,n)
