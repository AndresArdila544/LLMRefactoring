```python
integer = int(input())
cout = []
i = 1
while i <= integer:
    x = i
    while x > 0 and not (x % 3 == 0):
        if x % 10 == 3:
            cout.append(i)
        x //= 10
    i += 1
print(' '.join(str(n) for n in cout))
```