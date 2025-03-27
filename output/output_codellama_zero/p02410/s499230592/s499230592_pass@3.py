n, m = map(int, raw_input().split(" "))
a = []
for i in range(0, n):
	b = map(int, raw_input().split(" "))
	a.append(b)
for j in range(0, m):
	k = input()
	for i in range(0, n):
		a[i][j] = a[i][j] * k
s = 0
for i in range(0,n):
	for j in range(0,m):
		s += a[i][j]
print str(s)