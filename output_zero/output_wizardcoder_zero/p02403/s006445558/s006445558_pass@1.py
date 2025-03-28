```python
while True:
    a, b = map(int, input().split())
    if a and b:
        for i in range(a):
            print('#'*b)
    elif not (a or b) or not all([a == 0, b == 0]):
        break
```