```python
while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    elif x >= y:
        print(y, x)
    else:
        print(x, y)
```

The original code works as intended. It takes two integers from the user input, `x` and `y`, and swaps their values if `x` is greater than or equal to `y`. If not, it prints them in their original order.

However, I have added an `elif` statement instead of an `if-else` block for better clarity. Additionally, I removed the unnecessary parentheses around the condition of the `break` statement.