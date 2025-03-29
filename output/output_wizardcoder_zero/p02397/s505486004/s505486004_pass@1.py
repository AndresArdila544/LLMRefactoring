```python
while True:
    x,y = map(int, input().split())
    if not all([x,y]): break
    print((y,x) if x >= y else (x,y))