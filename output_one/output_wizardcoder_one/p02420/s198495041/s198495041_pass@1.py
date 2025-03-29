```python
while True :
    C = input()
    if C == "-":
        break
    else:
        m = int(input())
        h = int(input())
        for i in range(m):
            c = input()
            C = C[0:h] + c + C[h:]
print(C)
```