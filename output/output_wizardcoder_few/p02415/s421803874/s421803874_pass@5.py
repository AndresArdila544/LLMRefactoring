x = input()
ans = ''
for v in x:
    if str.isupper(v):
        ans += str.lower(v)
    elif str.islower(v):
        ans += str.upper(v)
print(ans)