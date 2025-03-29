n, m = map(int, input().split())
print(*[2*i + i*2 for i in range(1, n+1)], sep='\n')