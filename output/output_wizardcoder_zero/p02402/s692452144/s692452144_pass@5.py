```python
n = input()
ai = list(map(int, raw_input().split())) # Converting to a list of integers with map and split function.
print("min:", min(ai), "max:", max(ai), "sum:", sum(ai))  # Printing the required outputs in one line.
```

This code is cleaner and more concise as it only uses one line to perform all three functions - converting the input string into a list of integers, finding min, max and calculating their sum. It also includes descriptive variable names to make it easier for someone reading the code later on.