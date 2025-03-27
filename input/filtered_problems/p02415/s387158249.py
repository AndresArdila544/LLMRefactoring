s1 = input()
s2 = ''
for c in s1:
    if ord('a') <= ord(c) <= ord('z'):
        c0 = chr(ord(c) - ord('a') + ord('A'))
    elif ord('A') <= ord(c) <= ord('Z'):
        c0 = chr(ord(c) - ord('A') + ord('a'))
    else:
        c0 = c
    s2 += c0
print(s2)
