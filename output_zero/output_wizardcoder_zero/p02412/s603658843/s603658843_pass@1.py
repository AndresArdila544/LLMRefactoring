```python
while True:
    n, x = map(int, input().split()) # use map to convert input strings into integers for both n and x
    if n == 0 and x == 0:
        break
    cnt = 0
    for a in range(1, n):
        ab = a + a+1
        for b in range(a+1, n):
            abc = ab + b
            if abc >= x:
                cnt += 1
                break
            for c in range(b+1, n):
                if abc == x:
                    break
                elif abc > x:
                    break
        print(cnt)
```

```python
while True:
    try:  # use a try-except block to catch the EOFError exception that occurs when we reach the end of file (n and x will be NoneType after that point)
        n, x = map(int, input().split()) # use map to convert input strings into integers for both n and x
        if not n or not x:  # check if n and x are both non-zero
            break
    except EOFError:
        break
    
    cnt = 0
    for a in range(1, n):
        ab = a + 1
        for b in range(a+1, n):
            abc = ab + b
            if abc >= x:
                break
        else: # use the "else" clause to run this block only when we have completed all loops without encountering a "break"
            cnt += 1
    print(cnt)
```