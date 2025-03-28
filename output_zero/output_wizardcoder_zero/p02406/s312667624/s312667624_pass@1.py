```python
integer = int(input())
cout = []

for i in range(1, integer+1):
    x = i
    if x % 3 == 0 or (x // 10) % 3 == 0:
        cout.append(i)
    
print(' '.join(str(num) for num in cout))
```