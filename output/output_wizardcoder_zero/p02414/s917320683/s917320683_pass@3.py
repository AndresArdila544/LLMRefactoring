n, m, l = map(int, input().split())
nm = [[int(input()) for _ in range(m)] for i in range(n)]
ml = [[int(input()) for _ in range(l) for j in range(m)]]
matrix = [sum(row * col for row, col in zip(*[nm, ml])] for i in range(n)]
print(" ".join(str(sum_) for sum_ in matrix))