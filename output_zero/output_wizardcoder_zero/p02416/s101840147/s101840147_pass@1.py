```python
while True:
    input_ = int(input())
    if input_ == 0: break
    print(sum(map(int, str(input_)))
```

The code takes a string of digits and converts it to an integer using the `int()` function before summing its digits. If the user enters '0', it breaks out of the loop. Otherwise, it prints the sum of all the digits in the input. The `map(int, str(input_))` function is used to convert each character in the string to an integer and then `sum` adds them up. The `raw_input()` function has been replaced with `input()`.