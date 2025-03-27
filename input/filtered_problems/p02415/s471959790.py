S = input()

ans = ''
for s in S:
    ans += s.lower() if s.isupper() else s.upper()

print(ans)
