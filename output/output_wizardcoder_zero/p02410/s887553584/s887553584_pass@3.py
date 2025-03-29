n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)] # use a list comprehension to create A and initialize b
b = list(map(int, input().split()) for i in range(m))