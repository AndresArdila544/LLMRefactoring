```python
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    for i in range(a):
        print('#' * (i == 0 or i == a - 1) + '.' * (b - 2) + '#', end='')
    print()
```

Explanation: The program takes two integers as input, `a` and `b`, which represent the number of rows and columns to be printed. It then prints a pyramid-like structure with `#` characters for each row. If `i` is 0 or the last row (which is `a - 1`), it prints only `#`. Otherwise, it prints `#` followed by `.` and `#`, repeated `b - 2` times. Finally, it moves to the next line. The `end=''` parameter in the print statements prevents a newline from being printed after each character, allowing us to concatenate them with `+`. The code is more concise than the original version using fewer lines and improved readability.