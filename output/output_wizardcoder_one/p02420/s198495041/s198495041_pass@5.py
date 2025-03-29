```python
while True :
    C = input()
    if C == '-':
        break
    else:
        m = int(input())
        for i in range(m):
            h = int(input())
            c = input()
            C += c * h
print(C)
```