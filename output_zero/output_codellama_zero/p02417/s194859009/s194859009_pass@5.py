import sys
dict = {}
lines = sys.stdin.readlines()
for line in lines:
    for i in range(len(line)):
        c = line[i].lower()
        if ord(c) >= 97 and ord(c) <= 123:
            dict[c] += 1

l = list(dict.items())
for i in l:
    print(f'{i[0]} : {i[1]}')