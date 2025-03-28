Here is the refactored Python program:

n,m = map(int,raw_input().split())
a = [[int(x) for x in raw_input().split()] for i in range(n)]
for j in range(m):
	k = input()
	for i in range(n):
		a[i][j] *= k
for i in range(n):
	print sum(a[i])