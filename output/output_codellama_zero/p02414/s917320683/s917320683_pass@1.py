n, m, l = map(int, input().split())
nm = [[int(x) for x in input().split()] for _ in range(n)]
ml = [[int(x) for x in input().split()] for _ in range(m)]
matrix = []
for i in range(n):
	lista = [sum(x*y for x, y in zip(nm[i], ml[k])) for k in range(m)]
	matrix.append(lista)
for i in range(n):
	text = "".join(str(x) + " " for x in matrix[i])[:-1]
	print(text)