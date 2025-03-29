```python
def multiply_and_double(a, b):
    return a * b * 2 + a + b


if __name__ == "__main__":
    print(multiply_and_double(*map(int, input().split()))
```

This code is more concise and does the same thing as the original program. It takes two integers as inputs separated by spaces, multiplies them, doubles the result, and prints it to the console. Instead of using separate variables for a and b, they are passed directly into the function as arguments and unpacked with the `*map` function.