```python
while True:
    C = input()
    if C == "-":
        break
    else:
        m = int(input())
        for i in range(m):
            h = int(input())
            c = C[:h] + C[h:]
            print(c)
```