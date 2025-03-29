counter = 1
while True:
    x = input()
    if x == '0':
        break
    print("Case {}: {}".format(counter, x)
    counter += 1

Refactored version:

counter = 1
while True:
    x = input()
    if x != '0':
        print("Case {}: {}".format(counter, x)
        counter += 1