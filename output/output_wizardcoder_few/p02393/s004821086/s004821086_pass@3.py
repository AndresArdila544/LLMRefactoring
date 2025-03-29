```python
a,b,c = map(int,input().split())
if a < b :
    if a > c:
        a, b = a^b, a^c ^ b
    elif b > c:
        a, b = a^b, a^c
print(a,b,c)
```