refactored_code = '''import math
r,c=map(int,input().split())
a=[list(map(int, input().split())) for i in range(r)]
for row in a:row+=[sum(row)
print(*row); row.pop()
a=zip(*a[::-1])
for i in range(c): print(sum(i), end=' ')
print(sum(a[0]))'''