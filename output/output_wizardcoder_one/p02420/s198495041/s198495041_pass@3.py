```python
while True:
    C = input()
    if C == "-":
        break
    else:
        m = int(input())
        for i in range(m):
            h = int(input())
            c = input()[0 : h]
            C += c + input()[h:]
        print(C)
```