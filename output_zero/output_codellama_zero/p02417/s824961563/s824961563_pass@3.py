import re
while True:
    a = input()
    if not a: break
    b = a.lower()
    for letter in string.ascii_letters:
        print(letter+':',end=' ')
        count = sum([1 for c in b if c==letter])
        print(count)