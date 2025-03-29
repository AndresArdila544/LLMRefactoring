```python
while True:
    alp = input()
    if alp == '-':
        break

    m = int(input())
    h = int(input())
    alp = alp[h:] + alp[:h]
    print(alp)
```