```python
r, c = map(int, input().split())
a = [list(map(int, input().split())) for i in range(r)]
b = [[0] * (c + 1) for i in range(r + 1)]
for row_num in range(len(a)):
    b[row_num][:c+1] = a[row_num]
    b[0][row_num] += sum(a[row_num])
    b[-1][row_num] += sum(a[row_num])
    b[row_num][-1] += sum(a[row_num])
for row in b:
    print(*row)
```