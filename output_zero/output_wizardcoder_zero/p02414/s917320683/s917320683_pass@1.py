n, m, l = map(int, input().split())
nm_list, ml_list = [], []
for _ in range(n): nm_list += [list(map(int, input().split()))]
for _ in range(m): ml_list += [list(map(int, input().split())] 
matrix = [[sum(nm[i][k]*ml[k][j] for k in range(m)) for j in range(l)] for i in range(n)]
for row in matrix: print(" ".join(str(x) for x in row))