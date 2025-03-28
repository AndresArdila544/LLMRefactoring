count = 0
while True:
    try:
        x = int(input())
        if x == 0:
            break
        print("Case {}: {}".format(count + 1, x))
        count += 1
    except ValueError:
        pass