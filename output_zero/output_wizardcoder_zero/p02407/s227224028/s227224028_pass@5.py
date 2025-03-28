```python
n = int(input())
var = input().split()
print(" ".join([str(var[i-1]) for i in range(n, 0, -1) if i == 0][0])
```

This code achieves the same functionality as the original program but is more concise and faster. It uses a list comprehension to iterate through the indices of `var` starting from n-1 to 0, and joins all elements using " " " as a separator, which gives us the desired output. The resulting string is printed without any need for an if statement or a while loop.