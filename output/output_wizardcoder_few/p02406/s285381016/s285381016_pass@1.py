The original program is already quite concise and easy to read, so there's not much to refactor in this case. However, here's a minor improvement I can suggest:

```python
a = []
n = int(input())
for i in range(1, n+1):
    if i % 3 == 0 or '3' in str(i):
        a.append(i)
print(' ', end='')
print(*a)
```
This will have the same output as the original program but use fewer lines and make it more Pythonic. The `c` variable and incrementing `i` is not necessary, so I removed them.