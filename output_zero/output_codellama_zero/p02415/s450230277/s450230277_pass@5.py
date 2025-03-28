Here is the refactored version of the code:

I=raw_input()
O=(''.join(c.lower() if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" else c.upper() for c in I))
print O