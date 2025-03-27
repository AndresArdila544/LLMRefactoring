Here is the refactored code:
n, m = map(int, input().split())
arrs = []
for _ in range(n):
    vector = list(map(int, input().split()))
    arrs.append(vector)

for arr in arrs:
    c=0
    for i, scalar in enumerate(arr):
        c += scalar * m[i]
    print(c)