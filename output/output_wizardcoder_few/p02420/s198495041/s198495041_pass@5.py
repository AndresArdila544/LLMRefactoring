```python
def reverse_string(s):
    return s[::-1]

while True :
    C = input()
    if C == "-":
        break
    else:
        m = int(input())
        for i in range(m):
            h = int(input())
            c = input()[0:h]
            C += c + reverse_string(c)
        print(C.rstrip("-"))
```