n, m = map(int, input().split())
arrs = [list(map(int, input().split())) for _ in range(n)]
vector = list(map(int, input().split()))
[print(sum(arr_i * vector_i) for arr_i in arrs) for vector_i in vector]