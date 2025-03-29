```python
while True:
    alp = input()
    if alp == '-':
        break
    m = int(input())
    for i in range(m):
        h = int(input())
        alp = alp[h:] + alp[:h]  # Use slicing to reverse the string and concatenate it with itself
    print(alp)
```