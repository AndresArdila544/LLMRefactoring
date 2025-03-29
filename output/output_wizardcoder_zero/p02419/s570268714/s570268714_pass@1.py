```python
w = input()
print(sum(1 for _ in [p.lower() == w for p in map(str.strip, iter(input(), '')) if p != "END_OF_TEXT"])