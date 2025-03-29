```python
s = input() * 2
p = input()
if p in s:
    print('Yes')
else:
    print('No')
```

Refactored version (with fewer lines and improved readability):

```python
print('Yes' if input() * 2 == input() else 'No')
```