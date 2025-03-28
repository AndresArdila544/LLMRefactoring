s = str(input())

q = int(input())

d_list=[]
for i in range(q):
  s2 = ''
  
  d = list(map(str, input().split()))
  if d[0] == 'print':
    print( s[ int(d[1]): int(d[2])+1 ] )
    
  elif d[0] == 'reverse':
    S = list(s)
    S[int(d[1]):int(d[2])+1] = reversed(S[int(d[1]):int(d[2])+1])
    for i in S:
      s2 += i
    s = s2
   
  elif d[0] == 'replace':
    S = list(s)
    S[int(d[1]):int(d[2])+1] = list(d[3])
    for i in S:
      s2 += i
    s = s2
