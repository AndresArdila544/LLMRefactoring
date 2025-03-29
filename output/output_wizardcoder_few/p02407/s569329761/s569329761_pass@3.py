```python
n = int(input())
an = input().split()
out_c1 = ''
for a in reversed(an):
    out_c1 += '{} '.format(a)
print(out_c1[:-1])
```