```python
a, b = map(int, input().split()) # Refactored code without introductions and comments.
print("{0} {1} {2:.7f}".format(*map(str,(a//b, a%b, round(float(a)/float(b), 7)))).replace(',', ''))
```

Explanation: 
We can use `input` instead of `raw_input` and `map` to convert user input from string to integer. We then create a tuple of the three variables we want to print by using the `str.format` method with an asterisk before the argument map. Finally, we replace any commas in the output string with empty space.