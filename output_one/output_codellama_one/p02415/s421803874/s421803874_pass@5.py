x = input()
ans = ''
for v in x:
    if str.isupper(v):
        ans += v.lower()
    elif str.islower(v):
        ans += v.upper()
    else:
        ans += v
print(ans)