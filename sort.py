tscores = [3, 4, 7, 4, 2, 7, 46, 12, 8, 43, 6, 2, 45, 12, 3, 32, 23, 8, 56, 1]
c=0



def merge(ten_s, ten_t, gpa_s, gpa_t):
	n = len(s) + len(t)
	s.append(float("inf"))
	t.append(float("inf"))

	for i in range(0, n):
		



def merge(s,t, index_s, index_t, count):
	n = len(s) + len(t)
	v = [None]*n
	index_v = [None]*n
	s.append(float("inf"))
	t.append(float("inf"))

	for i in range(0,n):
		if(len(index_s)>0 and len(index_t)>0):
			print (s[0], index_s[0]), (t[0], index_t[0])
			if(s[0]>t[0]):
				if(index_s[0]<index_t[0]):
					count+=1
			elif(s[0]<t[0]):
				if(index_s[0]>index_t[0]):
					count+=1
		print count
		if s[0] < t[0]:
			v[i] = s.pop(0)
			index_v[i] = index_s.pop(0)
		else:
			v[i] = t.pop(0)
			index_v[i] = index_t.pop(0)
	return v, index_v, count

def sort(s):
	count = 0
	q = []
	indices = []
	for i in range(0, len(s)):
		q.append([s[i]])
		indices.append([i])
	while(len(q) >=2):
		u = q.pop(0)
		v = q.pop(0)
		u_index = indices.pop(0)
		v_index = indices.pop(0)
		out1, out2, out3 = merge(u,v, u_index, v_index, count)
		q.append(out1)
		indices.append(out2)
		count = out3
	if(q == []):
		return []
	else:
		return q[0], indices[0], count

print sort(tscores)



