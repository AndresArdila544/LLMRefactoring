while True:
    try:
        a, b = map(int, input().split())
    except ValueError:
        break
    if a == 0:
        break
    print('#'*b)
    print()