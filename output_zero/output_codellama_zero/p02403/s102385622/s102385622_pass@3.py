Here is the refactored version of your original Python program:

while True:
    h, w = map(int, input().split())
    if not h and not w:
        break
    print('#' * w)
    print()