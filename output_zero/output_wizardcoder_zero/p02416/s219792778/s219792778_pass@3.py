```python
def sum_digits(n):
    return sum(map(int, str(n)))

while True:
    n = int(input())
    if n == 0:
        break
    print(sum_digits(n))
```