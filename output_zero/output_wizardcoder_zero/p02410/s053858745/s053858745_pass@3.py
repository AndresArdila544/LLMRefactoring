n, m = map(int, input().split())
vector_list = []
for i in range(n):
    vector_list.append([int(x) for x in input().split()])
scalar_list = [int(input()) for _ in range(m)]
for arr in vector_list:
    print(sum(a*b for a, b in zip(arr, scalar_list)))