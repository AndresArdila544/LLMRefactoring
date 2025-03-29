```python
def sum_digits(n):
    return sum(map(int, str(n)))


while True:
    s = input()
    if s != '0':
        print(sum_digits(s))
    else:
        break
```