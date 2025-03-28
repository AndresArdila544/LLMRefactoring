```python
n = int(input())
a = map(int, raw_input().split())
while n > 0:
    print a[n-1],
    n -= 1 
```

The code simply takes an input integer `n` and reads in a list of integers separated by spaces as `a`, then prints the last element in `a` using `print a[n-1]`, decrementing `n` each time until it reaches 0. It can be simplified to:

```python
n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    print(a[i])
```

This code also uses the `input()` function instead of `raw_input()` and converts the input to a list using `list()`. This is more Pythonic and easier to read.