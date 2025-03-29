n, m = map(int, input().split())
 A = list()
 for i in range(n):
     A.append(list(map(int, input().split())))
 B = [int(input()) for i in range(m)]
 res = [sum(x*y for x, y in zip(A[i], B)) for i in range(n)]
 print(*res, sep='\n')