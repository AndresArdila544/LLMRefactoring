```python
def multiply(a, b):
    return a * b

def double_sum(a, b):
    return 2 * (a + b)

if __name__ == "__main__":
    l = input().split()
    a, b = map(int, l)
    print(multiply(a[0], b[0]), double_sum(a[0], b[1]))
```