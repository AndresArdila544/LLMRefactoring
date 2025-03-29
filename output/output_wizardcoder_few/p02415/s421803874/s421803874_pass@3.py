Here's the refactored version of the given Python program:

```python
x = input()
ans = ''
for v in x:
    ans += ''.join(['' if str.isupper(v) else ''.join([str.lower(v), '', ''])[0] for v in x])
print(ans)
```