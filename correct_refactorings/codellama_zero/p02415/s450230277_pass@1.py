I=raw_input()
O=""
for i in I:
	O+=(i.lower() if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" else i.upper())
print O