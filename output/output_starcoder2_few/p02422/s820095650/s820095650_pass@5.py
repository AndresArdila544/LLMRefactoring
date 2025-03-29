Refactored version:


import sys
for line in sys.stdin:
  s = str(line)
q  = int(input())

for i in range(q):
  
  d=list(map(str, input().split()))

  if d[0] == 'print':
    print(s[int(d[1]):int(d[2])+1])
  
  elif d[0] == 'reverse':
    S = list(s)
    S[ int(d[1]):int(d[2])+1 ]  = reversed(S[int(d[1]):int(d[2])+1 ])
    for i in S:
      s += i
    
  elif d[0] == 'replace':
    S=list(s)
    S[int(d[1]): int(d[2]) + 1 ] = list(d[3])
    for i in S:
      s+=i


Original version:

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
for line in sys.stdin:
  s=str(line)
  
q  = int(input())
d_list=[]
for i in range(q):
  
  d=list(map(str, input().split()))

  if d[0] == 'print':
    print(s[int(d[1]):int(d[2])+1])
  elif d[0] == 'reverse':
    S = list(s)
    S[ int(d[1]):int(d[2])+1 ]  = reversed(S[int(d[1]):int(d[2])+1 ])
    for i in S:
      s += i
  elif d[0] == 'replace':
    S=list(s)
    S[int(d[1]): int(d[2]) + 1 ] = list(d[3])
    for i in S:
      s+=i

Refactored version:

import sys
for line in sys.stdin:
  s=str(line)
  
q  = int(input())
d_list=[]
for i in range(q):
  
  d=list(map(str, input().split()))

  if d[0] == 'print':
    print(s[int(d[1]):int(d[2])+1])
  elif d[0] == 'reverse':
    S = list(s)
    S[ int(d[1]):int(d[2])+1 ]  = reversed(S[int(d[1]):int(d[2])+1 ])
    for i in S:
      s += i
  elif d[0] == 'replace':
    S=list(s)
    S[int(d[1]): int(d[2]) + 1 ] = list(d[3])
    for i in S:
      s+=i