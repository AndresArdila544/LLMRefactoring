```python
a, op, b = map(int, input().split())

while True:
    if op == "?":
        break
    
    if op == "+":
        a += b
    elif op == "-":
        a -= b
    elif op == "*":
        a *= b
    elif op == "/":
        a //= b
        
    print(a)
    a, op, b = map(int, input().split())
```