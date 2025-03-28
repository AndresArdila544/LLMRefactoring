x = input()
for i in range(len(x)):
    if x[i].isupper():
        ans += x[i].lower()
    elif x[i].islower():
        ans += x[i].upper()
    else:
        ans += x[i]
print(ans)