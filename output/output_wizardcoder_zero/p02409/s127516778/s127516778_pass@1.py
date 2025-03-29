```python
for i in range(int(input())):
    b, f, v = map(int, input().split())
    B[b - 1][f - 1] += v
    
print('#' * 20)
for row in B[:-1]: # skips the first row, since it is a separator
    for col in row:
        print(' ', end='')
        print(*col)
```