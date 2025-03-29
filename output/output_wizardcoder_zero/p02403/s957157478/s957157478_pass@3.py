```
sides = [int(x) for x in input().split()]
while sides != [0, 0]:
    print('#' * sides[1])
    for _ in range(sides[0]):
        print(' ' * (sides[1]), end='')
        print('#' * sides[1])
```