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
    x = ord(t[i])
    if x>96 and x<123:
        y[x-97] += 1
for i in range (97,123):
    print(chr(i), ":", y[i-97])
