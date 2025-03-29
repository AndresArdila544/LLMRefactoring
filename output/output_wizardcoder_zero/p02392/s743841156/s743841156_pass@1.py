```python
def is_less_than(a, b):
    return a < b


def check_range(a, b, c):
    return is_less_than(a, b) and is_less_than(b, c)

a, b, c = map(int, input().split())
if check_range(a, b, c):
    print('Yes')
else:
    print('No')