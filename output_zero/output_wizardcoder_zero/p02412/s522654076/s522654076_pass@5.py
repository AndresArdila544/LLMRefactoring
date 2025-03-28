```python
a, b = map(int, input().split())
while a != 0 and b != 0:
    count = sum((i + j + k == b for i in range(1, a) for j in range(i+1, a) for k in range(j+1, a))
    print(count)
    a, b = map(int, input().split())