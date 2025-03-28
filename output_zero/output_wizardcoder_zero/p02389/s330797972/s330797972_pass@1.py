```python
num = input()
a, b = map(int, num.split())
print(*[a*b, a*(2)+b*(2)]) # print(a*b, end=" "), print(a*(2+b)*2)
```