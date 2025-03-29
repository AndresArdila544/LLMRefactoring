```python
a, b = map(float, input().split())
d, r = divmod(a,b)
print('{0:.8f} {1:.8f}'.format(a/b, a%b))