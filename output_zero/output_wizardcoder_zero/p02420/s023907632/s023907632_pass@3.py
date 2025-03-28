def shuffle_string(s):
    while s[0] != '-':
        for _ in range(int(input())):
            string = list(input())
            s = ''.join([string.pop(0), *string])
    return s