```python
c, r = map(int, input().split())
last_list = [0] * r
for i in range(c):
    x = input()
    s = sum(map(int, x.split()))
    last_list[i%r] += s
    print(x)
    print(s + (last_list[i % r - 1] if i > 0 else 0), end=" ")
print(*last_list, sum(last_list))
```