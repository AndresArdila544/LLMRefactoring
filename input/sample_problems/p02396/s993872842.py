counter = 1
while True:
    x = input()
    if x == '0':
        break
    else:
        print("Case {}: {}".format(counter, x))
        counter += 1
