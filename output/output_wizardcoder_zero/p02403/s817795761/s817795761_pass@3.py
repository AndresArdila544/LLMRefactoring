h, w = map(int, input().split())
while h != 0 or w != 0:
    for i in range(h):
        for j in range(w):
            print('#', end='')
        print()
    h, w = map(int, input().split()) 

# The above code is more concise and readable. It uses a single loop to handle both height and width inputs instead of nested loops, which reduces the lines of code by half.