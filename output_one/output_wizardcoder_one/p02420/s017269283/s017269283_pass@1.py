```python
while True:
    alp = input()
    if alp == '-':
        break
    
    m = int(input())
    for i in range(m):
        h = int(input())
        alp = alp[h:] + alp[:h]  # refactored using slicing to reverse the string
    print(alp)
```