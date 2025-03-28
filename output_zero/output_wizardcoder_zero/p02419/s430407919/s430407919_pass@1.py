```python
W = input().lower()
count = 0
while True:
    T = input().lower()
    if T == 'END_OF_TEXT':
        break
    count += T.split().count(W)
print(count)
```