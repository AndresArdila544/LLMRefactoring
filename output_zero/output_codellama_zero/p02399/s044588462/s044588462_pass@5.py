import sys
a,b = map(int,sys.stdin.readline().split())
d = a//b
r=a%b
f=a/b
print(str(d)+' '+str(r)+' '+str(f))