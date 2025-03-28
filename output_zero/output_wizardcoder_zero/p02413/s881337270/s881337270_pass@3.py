r, c = map(int, input().split())
arr = []
total_sums = [0] * (c + 1)
for _ in range(r):
    row = list(map(int, input().split()))
    arr.append(row + [sum(row)])
    for i in range(c+1):
        total_sums[i] += row[i]
        
print(" ".join(str(val) for sublist in arr for val in sublist[:-1]))
print(" ".join(str(total_sums[i]) for i in range(c+1)))