```python
n=int(input())
for _ in range(4):
    for _ in range(10):
        print(" ", end="")
    print()
for i in range(n):
    a,b,c,d = map(int, input().split())
    a-=1; b-=1; c-=1
    a[a][b][c] += d
print_grid = lambda x: ' '.join([str(sum(sum(row)) for row in x])
for i in range(4):
    print(print_grid(a) if i!=3 else print_grid(a)+' ########')
```