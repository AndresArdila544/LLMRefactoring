```python
def f(a, b):
    for i in range(a):
        k = b // 2
        if i % 2 == 0: #偶数
            print("#." * (k + (1 if b % 2 == 0 else 0) + 1)
        else: #奇数
            print(".#" * (k + (1 - (b % 2)) + (1 if b % 2 != 0 else 0))

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    for i in range(len(L)-1):
        f(a[i][0], a[i][1]) 
```

This should be the refactored version of the code with fewer lines and improved readability.
```python
while True:
    try:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break
        f(a,b)
    except ValueError:
        continue
``` 
This code will take the inputs for `a` and `b`, and then call the function `f()` with those values. If either of them is 0 or if there's an invalid input, it will stop asking for more inputs. The try-except block will catch any ValueError raised by map() when trying to convert the input to integers.