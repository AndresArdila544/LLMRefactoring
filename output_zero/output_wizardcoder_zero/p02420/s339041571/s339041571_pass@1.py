```python
while True:
    line = input()
    if line == '-': break
    for _ in range(int(input())):
        h = int(input())
        line = line[h:] + line[:h]
print(line)
```