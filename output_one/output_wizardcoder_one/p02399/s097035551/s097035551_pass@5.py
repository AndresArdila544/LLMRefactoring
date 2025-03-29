```python
a, b = map(int, input().split())
print(float(a) / b if a % b == 0 else a // b)
```

Explanation: 
- We use `map()` to convert the input values from string to integers.
- Then we print the result of the division, which is calculated using the `if` statement. If `a` is divisible by `b`, then it will print the result as a float (`float(a) / b`). Otherwise, it will print the floor division (`a // b`) since `//` operator returns an integer value.
- The output of both lines will be different if `a % b != 0`. For example:
```python
a = 7
b = 3
print(float(a) / b) # Output: 2.3333333333333333333335
print(a // b)   # Output: 2