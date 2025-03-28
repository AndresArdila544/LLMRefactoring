```python
def is_in_ascending_order(a, b, c):
    return a < b and b < c

a, b, c = map(int, input().split())
print('Yes' if is_in_ascending_order(a, b, c) else 'No')