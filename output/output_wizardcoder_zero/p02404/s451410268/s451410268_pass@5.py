```python
while True:
    num = [int(i) for i in input().split()]
    H, W = num[0], num[1]
    if W == 0 or H == 0:
        break
    print("#" * W + "\n")
    (print("." * (W - 2) + "#\n") * (H - 2))
    print("#" * W)
```
```python
while True:
    H, W = map(int, input().split())
    if not all(num > 0 for num in [W, H]:
        break
    print("#" * W + "\n")
    (print("." * (W - 2) + "#\n") * (H - 2))
    print("#" * W)
``` 
```python
while True:
    H, W = map(int, input().split())
    if not all(num > 0 for num in [W, H]:
        break
    for _ in range(H - 2):
        print("#" + "." * (W - 2) + "#\n")
    print("#" * W)
``` 
```python
while True:
    H, W = map(int, input().split())
    if not all(num > 0 for num in [W, H]:
        break
    for _ in range(H - 2):
        print("#" + "." * (W - 2) + "#\n")
print("#" * W)
``` 
```python
while True:
    try:
        H, W = map(int, input().split())
        if not all(num > 0 for num in [H, W]:
            break
        print("#" * W + "\n")
        for _ in range(H - 2):
            print("#" + "." * (W - 2) + "#\n")
    except ValueError:
        continue
print("#" * W)
``` 
```python
while True:
    try:
        H, W = map(int, input().split())
        if not all(num > 0 for num in [H, W]:
            break
        print("#" * W + "\n")
        for _ in range(H - 2):
            print("#" + "." * (W - 2) + "#\n")
    except ValueError:
        continue
print("#" * W)
```