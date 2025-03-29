# coding: utf-8
# Your code here!

t = ""
y = [0]*26
while True:
    try:
        n = input()
        m = str(n)
        m = m.lower()
        t += m
    except:
        break
for i in range(len(t)):
    if ord(t[i]) >= 97 and ord(t[i]) <= 123:
        y[ord(t[i]) - 97] += 1
for i in range(97,123):
    print(chr(i), ":", y[i-97])