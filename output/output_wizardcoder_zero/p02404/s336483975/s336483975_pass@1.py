```python
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    for i in range(a):
        print('#'*(i == 0 or i == a-1), end='')
        for _ in range(b-2):
            print('.', end='')
        print('#', end='' if i != a-1 else '\n')
``` 
This is the refactored version of the code, where I have used ternary operator to reduce the lines and improve readability.