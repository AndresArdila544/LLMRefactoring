```python
a = []
while True:
    try:
        tmp = int(input())
        if tmp == 0:
            break
        a.append(tmp)
    except ValueError:
        continue
for index, value in enumerate(a):
    print(f'Case {index}: {value}')
```