Here is a simplified version:

while sides != [0,0]:
    print('#' * sides[1] + '\n' * sides[0])
    sides = list(map(int, input().split()))