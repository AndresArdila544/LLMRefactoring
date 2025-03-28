while True:
    try:
        x = int(input())
        if x > 0:
            print(sum([int(x[i]) for i in range(len(x))]))
        else:
            break
    except ValueError:
        break