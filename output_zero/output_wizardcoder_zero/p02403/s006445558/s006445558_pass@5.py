def print_pattern():
    while True:
        a, b = map(int, input().split())
        if a or b:
            for i in range(a):
                for j in range(b):
                    print("#", end="")
                print()
        else:
            break
print_pattern()