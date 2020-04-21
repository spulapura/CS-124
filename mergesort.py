def merge(s, t):
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


def sort(s):
  count = 0
  if(len(s) == 0):
    return [],0
  elif(len(s) == 1):
    return s, 0
  else:
    split = len(s)/2
    s1, count1 = sort(s[0:split])
    s2, count2 = sort(s[split:])
    v, count3 = merge(s1,s2)
  count = count1+count2+count3
  print v, count
  return v, count 


ten = [3, 4, 7, 4, 2, 7, 46, 12, 8, 43, 6, 2, 45, 12, 3, 32, 23, 8, 56, 1]

print sort(ten)