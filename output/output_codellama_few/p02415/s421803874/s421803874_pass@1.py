import re
x = input()
ans = re.sub(r"[a-z]", lambda x:x.group().upper(), re.sub(r"[A-Z]", lambda x:x.group().lower(), x))
print(ans)