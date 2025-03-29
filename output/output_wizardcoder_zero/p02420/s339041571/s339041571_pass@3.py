```python
while True:
    line = input()
    if line == '-':
        break
    h = int(input())
    line = line[h:] + line[:h]
    print(line)
```