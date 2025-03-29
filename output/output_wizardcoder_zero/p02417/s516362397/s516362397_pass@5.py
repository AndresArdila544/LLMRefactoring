import fileinput
T = [0] * 26
for line in fileinput.input():
    for c in map(ord, list(line)):
        if 65 <= c <= 90:
            T[c-65] += 1
        elif 97 <= c <= 1222:
            T[c-97] += 1
for i, count in enumerate(['A'] + [chr(i+65) for i in range(26)]):
    print(count, ":", T[i])
"""