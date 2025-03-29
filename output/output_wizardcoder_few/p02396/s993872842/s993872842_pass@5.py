counter = 1
while True:
    x = input()
    if x == '0':
        break
    print("Case {}: {}".format(counter, x)
    counter += 1
    
Refactored version:

for i in itertools.count():
    x = input()
    if x == '0':
        break
    print(f"Case {i + 1}: {x}")