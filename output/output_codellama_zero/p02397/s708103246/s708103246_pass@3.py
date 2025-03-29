Here is a refactoring of the original program that reduces its complexity and length:

while True:
    try:
        a,b = map(int, input().split())
        if not (a == 0 and b == 0):
            print(min(a,b), max(a,b))
    except EOFError:
        break