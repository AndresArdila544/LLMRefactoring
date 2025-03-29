x = input()
ans = ''
for v in x:
    if v.isupper():
        ans += v.lower()
    elif v.islower():
        ans += v.upper()
print(ans)