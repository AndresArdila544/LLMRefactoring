# coding: utf-8
# Your code here!

while True:
    try:
        n = input()
        m = str(n).lower()
        for i in range(len(m)):
            x = ord(m[i])
            if 97 <= x <= 123:
                y[x - 97] += 1
    except:
        break
for i in range(97, 123):
    print(chr(i), ":", y[i-97])