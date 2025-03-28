def checkio(n, x):
    return sum(1 for i in range(1, n+1) for j in range(i+1, n+1) for k in range(j+1, n+1) if i + j + k == x)