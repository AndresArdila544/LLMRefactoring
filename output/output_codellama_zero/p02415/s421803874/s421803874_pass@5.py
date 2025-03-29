```
import string
x = input()
ans = ''.join([v.lower() if v.isupper() else v.upper() for v in x])
print(ans)
```