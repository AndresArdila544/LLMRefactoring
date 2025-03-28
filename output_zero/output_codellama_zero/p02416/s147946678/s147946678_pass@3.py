Here is a more concise and readable version of the original program:

while True:
    x = input()
    if x == '0':
        quit()

    print(sum([int(y) for y in x]))