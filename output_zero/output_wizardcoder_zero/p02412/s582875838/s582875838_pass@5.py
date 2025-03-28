```python
def count_combinations(n, x):
    return sum([1 for i in range(1, n) for j in range(i+1, n) if j < x-i-j <= n])

while True:
    try:
        n, x = map(int, input().split())
        if n + x == 0:
            break
        print(count_combinations(n, x))
    except ValueError:
        pass
```

This code uses list comprehension to reduce the number of lines and improve readability. It also handles cases where non-integer inputs are entered.

The `count_combinations` function takes two arguments, `n` and `x`, and returns the number of combinations that satisfy the condition in the original code using a list comprehension instead of a nested loop. The `try` block handles any input errors and stops execution when `n + x == 0`.