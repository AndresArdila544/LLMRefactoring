```python
def check_triangle(a, b, c):
    return 'Yes' if a < b and b < c else 'No'

print(check_triangle(*map(int, input().split()))
```