```python
count = 0
while True:
    T = input()
    if T == 'END_OF_TEXT':
        break
    count += T.lower().split().count(W.lower())
print(count)
```

This code uses a `while` loop to iterate through user inputs, and increments the counter for each occurrence of `W` in each input until it encounters the `END_OF_TEXT` marker, which breaks out of the loop. It also converts all inputs and keywords to lowercase before counting the occurrences.

Note: The original code used a separate variable `T` to store the user input, but we can simplify this by just using a boolean flag to check for the end condition instead of storing it in another variable.