Refactored version:

while True:
    a = input()
    if '?' in a:
        break
    print(int(''.join([i for i in a.split()]))