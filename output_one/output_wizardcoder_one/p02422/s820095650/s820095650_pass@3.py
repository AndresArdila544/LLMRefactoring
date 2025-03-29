s = input()
q = int(input())

d_list=[]
for i in range(q):
  d = list(map(str, input().split()))
  if d[0] == 'print':
    print( s[int(d[1])-1: int(d[2]) ] )
    
  elif d[0] == 'reverse':
    S = list(s)
    S[int(d[1]):int(d[2])+1] = reversed(S[int(d[1]:int(d[2]+1))])
    s = "".join(S)
    
  elif d[0] == 'replace':
    S = list(s)
    if int(d[3]) != -1:
      for i in range(int(d[1]), int(d[2])+1):
        S[i] = d[4]
    else:
      for i in range(int(d[1]), len(s)):
        if i >= int(d[2] and i <= int(d[3]):
          S[i] = ''
    s = "".join(S)
  print(s)