```python
n = int(input())
tp = hp = 0
for _ in range(n):
    tw,hw = map(int, input().split())
    if tw == hw:
        tp += 1
        hp += 1
    elif tw > hw:
        tp += 3
    elif tw < hw:
        hp += 3
print(tp,hp)
```

In this program, we read an integer `n` from the user as input and then for each of the next `n` lines, we read a pair of integers separated by space. We check if they are equal, if yes, we add 1 to both `tp` and `hp`, else, we add 3 to `tp` if `tw` is greater than `hw`, or 3 to `hp` if `tw` is lesser than `hw`. Finally, we print the values of `tp` and `hp` separated by space.