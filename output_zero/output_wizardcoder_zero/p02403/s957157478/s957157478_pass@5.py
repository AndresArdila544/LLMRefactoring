sides = list(map(int, input().split()))
while sides != [0, 0]:
    print('#' * sides[1] + '\n' * sides[0])