S = input()
ans = ''.join([s.lower() if s.isupper() else s.upper() for s in S])
print(ans)