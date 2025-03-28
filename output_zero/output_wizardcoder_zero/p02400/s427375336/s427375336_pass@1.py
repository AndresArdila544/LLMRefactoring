You can use string formatting to combine the calculations instead of using multiple print statements:

```python
r = float(input())
print("{:.6f}".format(math.pi * r**2), "{:.6f}".format(2 * math.pi * r))