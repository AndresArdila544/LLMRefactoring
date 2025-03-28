Here is a refactored version of your program:

import re

I=raw_input()
O=re.sub('([a-z])|([A-Z])', lambda m:m.group().lower() if m.group(1) else m.group().upper(), I)
print O