```python
H, W = map(int, input().split())
table = [[0]*(W+1) for i in range(H+1)]
for row in range(H):
    a = list(map(int,input().split()))
    for col in range(W):
        table[row][col] = a[col]
         
for row in range(H):
    table[H].append(table[row][:W])
    table[:H+1].append([0]*(W+1))
         
for row in range(H+1):
    print(*table[row], sep=' ')
```