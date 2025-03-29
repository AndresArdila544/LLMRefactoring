```python
while True:
    m, f, r = map(int, input().split())
    if m == -1 and f == -1:
        break
    
    s = m + f
    
    if s < 30 or (m == -1 or f == -1):
        print('F')
    elif s < 50 and r >= 50:
        print('D')
    elif s < 65:
        print('C')
    else:
        print('B' if s < 80 else 'A')
``` 
```python
while True:
    m, f = map(int, input().split())
    if m == -1 and f == -1:
        break
    
    s = m + f
    
    if s < 30 or (m == -1 or f == -1):
        print('F')
    elif s >= 50:
        print('D' if r >= 50 else 'C')
    elif s < 65:
        print('B')
    else:
        print('A') 
```