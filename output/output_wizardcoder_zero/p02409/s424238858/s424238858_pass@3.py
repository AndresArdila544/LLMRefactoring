```python
rooms = [[0] * 10 for i in range(4) for j in range(3)]
n = int(input())
for l in range(n):
    a, b, c, d = map(int, input().split())
    rooms[a-1][b-1] += d
    
for row in rooms:
    for room in row:
        print(" ".join(str(room), end=" ")
    print()
        
    if row != [0] * 10:
        print("#" * 20
```