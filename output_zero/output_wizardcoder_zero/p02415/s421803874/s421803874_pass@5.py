```python
x = input()
ans = ''
for v in x:
    ans += (v if str.isupper(v) else v.lower()) + (v.upper() if not str.isupper(v) else '')
print(ans)
```