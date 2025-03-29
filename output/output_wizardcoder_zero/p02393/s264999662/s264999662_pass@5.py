One possible refactoring is to use conditional statements instead of if-elif chains, since all cases are mutually exclusive:
```python
a,b,c = map(int, input().split())
if a<=min(a,b):
    print(a, b, c)
else:
    print(max(a,b), min(a,b), c)  # the order of max and min does not matter for sorting purposes
```