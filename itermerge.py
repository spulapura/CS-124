def merge(s, t):
	s_len, t_len = len(s), len(t)
	print s, t
	count=0
	n = s_len + t_len
	v = []
	p = 0
	q = 0
	while(p<s_len and q<t_len):
		if t[q]<s[p]:
			v.append(t[q])
			q+=1
			count+=len(s)-p
		else:
			v.append(s[p])
			p+=1
	while(p<s_len):
		v.append(s[p])
		p+=1
	while(q<t_len):
		v.append(t[q])
		q+=1
	print v, count
	return v,count

def mergesort(s):
	count =0
	q=[]
	i=0
	for item in s:
		q.append([item])
	if len(s) == 0:
		return []
	if len(s) ==1:
		return s
	while(len(q[i]) < len(s)):
		print q
		list1 = q[i]
		list2 = q[i+1]
		merged_list, count2 = merge(list1, list2)
		q.append(merged_list)
		count+= count2
		i+=2
	return q[i], count


tscores = [3, 4, 7, 4, 2, 7, 46, 12, 8, 43, 6, 2, 45, 12, 3, 32, 23, 8, 56, 1]
print mergesort(tscores)




	