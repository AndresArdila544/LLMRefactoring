Here's a cleaner and more concise version of the program:

while True:
    x = input()
    if x > 0:
        print(sum([int(x[i]) for i in range(len(x))]))
    else:
        break