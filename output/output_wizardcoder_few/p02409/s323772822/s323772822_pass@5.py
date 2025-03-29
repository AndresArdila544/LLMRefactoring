```python
n = int(input())
for _ in range(n):
    b, f, r, v = map(int, input().split())
    a[b-1][f-1][r-1] += v

print('\n'.join([' '.join(' ' + str(sum(row)) for row in a]) + '\n' if i != 3 else '####################' for i, row in enumerate(a)])
```