from collections import deque

clock = 0
ten = [3, 4, 7, 4, 2, 7, 46, 12, 8, 43, 6, 2, 45, 12, 3, 32, 23, 8, 56, 1]
n=len(ten)
preorder = [0]*n
postorder = [0]*n
visited = [False]*n



def search(u, targets):
	visited[u] = True
	global clock
	pairs = deque([])
	for v in targets:
		if ten[v] < ten[u]:
			pairs.append(v)	
			clock +=1
		search(pairs.popleft(), pairs)

for v in range(0, n):
	if(visited[v] == False):
		search(v)


print clock








