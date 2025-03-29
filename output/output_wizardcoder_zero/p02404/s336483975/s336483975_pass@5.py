```python
def pyramid_pattern():
    while True:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break
        print('.' * (b-2) + '#' + '.' * (b-1), end='')
        print('#' + '.' * (b-2)) if i != a - 1 else None
    print()
```