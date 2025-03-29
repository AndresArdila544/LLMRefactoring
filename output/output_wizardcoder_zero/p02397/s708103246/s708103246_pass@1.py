```python
while True:
    a, b = map(int, input().split())
    if all([a == 0, b == 0]): break
    print(max(a,b), min(a,b))
```

The original program takes two integers as input and prints them in descending order. The refactored version uses the `map` function to convert the input strings into integers, then compares their values and prints the larger one first followed by the smaller one.

The if statement can be simplified using a list of booleans with `all()` to check for both conditions at once and avoid unnecessary repetition. The `max()` and `min()` functions are used to print them in descending order.