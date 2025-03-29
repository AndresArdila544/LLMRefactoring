I = input()
O=str()
for i in I:
    if i.isupper(): O += i.lower()
    elif i.islower(): O += i.upper()
print(O)