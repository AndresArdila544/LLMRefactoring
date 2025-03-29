import sys
def rotate_string():
    while True:
        s = input()
        if s == "-": break
        m = int(input())
        for i in range(m):
            h = int(input())
            s = s[h:] + s[:h]
        print(s)
rotate_string()