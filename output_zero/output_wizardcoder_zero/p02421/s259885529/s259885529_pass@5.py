```python
n = int(input())
Taro = 0
Hanako = 0
for i in range(n):
    t, h = input().split()
    x = 0
    for j in range(min(len(t), len(h)):
        if t == h:
            Taro += 1
            Hanako += 1
            x = 1
            break
        elif ord(t[j]) > ord(h[j]):
            Taro += 3
            x = 1
            break
        elif ord(t[j]) < ord(h[j]):
            Hanako += 3
            x = 1
            break
    if not x:
        Taro += max(len(t), len(h)) - min(len(t), len(h))

print("{} {}".format(Taro, Hanako))
```