#n,m = map(int, raw_input().split())
#line2 = map(int, raw_input().split())
#line3 = map(int, raw_input().split())


def mergeA(s, t):
  count=0
  n = len(s) + len(t)
  s.append(float("inf"))
  t.append(float("inf"))
  v =[]
  for i in range(0, n):
    if t[0] < s[0]:
      v.append(t.pop(0))
      count+= (len(s)-1)
    else:
      v.append(s.pop(0))
  return v, count


def sortA(s):
  count = 0
  if(len(s) == 0):
    return [],0
  elif(len(s) == 1):
    return s, 0
  else:
    split = len(s)/2
    s1, count1 = sortA(s[0:split])
    s2, count2 = sortA(s[split:])
    v, count3 = mergeA(s1,s2)
  count = count1+count2+count3
  return v, count 

def merge(s, t):
  count=0
  global m
  s_len = len(s)
  t_len = len(t)
  n = s_len + t_len
  s.append(float("inf"))
  t.append(float("inf"))
  v =[]
  m_index = [0]*(m+1) 
  p = 0
  q = 0
  while(p<s_len and q<t_len):
    if t[q][0] < s[p][0]:
      v.append(t[q])
      m_index[t[q][1]]+=1
      count+= (len(s)-p-1)
      q+=1
    else:
      v.append(s[p])
      if(m_index[s[p][1]] > 0):
        count-=m_index[s[p][1]]
      p+=1
  while(p<s_len):
    v.append(s[p])
    if(m_index[s[p][1]] > 0):
        count-=m_index[s[p][1]]
    p+=1
  while(q<t_len):
    v.append(t[q])
    q+=1

  return v, count


def sort(s):
  count = 0
  if(len(s) == 0):
    return [], 0
  elif(len(s) == 1):
    return s, 0
  else:
    split = len(s)/2
    s1, count1 = sort(s[0:split])
    s2, count2 = sort(s[split:])
    v, count3 = merge(s1, s2)
  count = count1+count2+count3
  print v, count
  return v, count 


line2 = [3, 4, 7, 4, 2, 7, 46, 12, 8, 43, 6, 2, 45, 12, 3, 32, 23, 8, 56, 1]
line3 = [3,5,1,0,3,5,2,1,0,1,2,4,3,5,5,1,2,3,2,2]

z= zip(line2, line3)
n = len(line2)
m=6
#ten= [3,4,7,4,2,7,46,12]
#line3=[3,5,1,0,3,3,5,1]
#ten_index = range(0,n)
#if(m == n):
#  print sortA(line2)[1]
#else:
print sort(z)[1]