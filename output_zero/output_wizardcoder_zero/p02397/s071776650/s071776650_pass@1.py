```python
li = []
while True:
    try:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break
        else:
            li.append([a,b])
    except ValueError:
        break
for pair in sorted(li):
    print(*pair)