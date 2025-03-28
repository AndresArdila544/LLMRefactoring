```python
W, H, x, y, r = map(int, input().split())
if all([x > 0, y > 0, x + r >= 0, y + r > 0, W - r - x >= 0, H - r - y >= 0]):
    print('Yes')
else:
    print('No')
``` 

Note that the `map()` function is not necessary for this specific example. It's used to convert each value from input() into an integer, but it can be replaced with tuple unpacking instead. Also, we can use a shorter boolean expression using the `all` function to check if all conditions are True.