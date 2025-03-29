```python
for i in iter(int, 0):
    print(f"Case {i}: {input()}")
```

This version of the program uses a generator object to replace the while loop and input function with an infinite loop that will break only when the user enters a 0. It then uses a for-loop to iterate over each integer input value, printing it with the case number using string formatting. The `iter(int, 0)` is a built-in Python function that generates infinite integers starting from 0 and stops at the first non-integer value entered by the user.

The only change made to the original code was changing the while loop into an infinite for-loop, and using string formatting to print the case number before each input.