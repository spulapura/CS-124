from collections import deque

n,m,q = map(int, raw_input().split())

comp_number = [None]*(n+1)
black = set([])
white = set([])
ccn = 0
for i in range(0,m):
	a,b = map(int, raw_input().split())
	if comp_number[a]==None and comp_number[b]==None:
		comp_number[a] = 

	







for i in range(0,q):
	t,a1,b1 = map(int, raw_input().split())
	if t == 2:
		if a1 in color:
			set_a = color[a1]
		else:
			set_a = None
		if b1 in color:
			set_b = color[b1]
		else:
			set_b = None
		if set_a == set_b and set_a != None:
			if a1 in color_sets[set_a][0] and b1 in color_sets[set_b][1]:
				count +=1
			elif a1 in color_sets[set_a][1] and b1 in color_sets[set_b][0]:
				count +=1
		#print count


print count



			



	