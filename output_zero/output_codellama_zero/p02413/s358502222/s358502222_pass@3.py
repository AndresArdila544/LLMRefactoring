Here is a refactored version of the program in fewer lines and more readable:
import os
r,c=map(int,input().split())
a=[list(map(int,input().split())) for i in range(r)]
b=[[0]*(c+1)for i in range(r+1)]

for i in range(r):
    for j in range(c):
        b[i][j]=a[i][j]

for i in b:
  print(*i)