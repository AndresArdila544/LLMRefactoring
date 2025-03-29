Here's a refactored version of the code you provided:

```python
while True:
    n = input()
    if n == '0 0': break
    x, y = map(int, n.split())
    print(max(x,y),' ',min(x,y))
```

This code reads a pair of numbers as input and prints the larger number followed by the smaller number (or vice versa) separated by a space. It also breaks out of the loop when the input is '0 0'. Note that I removed all the unnecessary variables and simplified the logic using built-in functions such as `max()` and `min()`. The refactored code has fewer lines, improved readability, and reduced complexity.