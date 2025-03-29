n, m = map(int, input().split())
A = [[int(x) for x in input().split()] for i in range(n)]
b = [int(x) for x in input().split()]
print('\n'.join([str(sum(x[i]*y for i, y in enumerate(b))) for x in A]))