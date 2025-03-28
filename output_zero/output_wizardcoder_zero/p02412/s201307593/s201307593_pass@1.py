def count_triplets(n, x):
    count = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            for k in range(j+1, n+1):
                if i + j + k == x:
                    count += 1
    return count 

while True:
    n, x = [int(_) for _ in input().split()]
    if not (n and x):
        break
    print(count_triplets(n, x))